import os
import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

ECS_CLUSTER = os.environ.get('ECS_CLUSTER')
ECS_SERVICE = os.environ.get('ECS_SERVICE')

ecs = boto3.client('ecs')

def lambda_handler(event, context):
    """Safe example: Inspect ECS service tasks and stop a single unhealthy task.

    Environment variables required:
    - ECS_CLUSTER
    - ECS_SERVICE

    Behavior:
    - Lists tasks for the service
    - Describes tasks and looks for STOPPED or UNHEALTHY tasks
    - Stops one unhealthy task so ECS can replace it

    This code is an example and should be adapted with proper IAM, retries, and safety checks.
    """
    logger.info('Received event: %s', event)
    cluster = ECS_CLUSTER or event.get('cluster')
    service = ECS_SERVICE or event.get('service')
    if not cluster or not service:
        logger.error('ECS_CLUSTER or ECS_SERVICE not set')
        return { 'status': 'error', 'reason': 'missing configuration' }

    # List running tasks for the service
    tasks_resp = ecs.list_tasks(cluster=cluster, serviceName=service, desiredStatus='RUNNING')
    task_arns = tasks_resp.get('taskArns', [])
    logger.info('Found %d running tasks', len(task_arns))

    if not task_arns:
        return { 'status': 'ok', 'message': 'no running tasks' }

    desc = ecs.describe_tasks(cluster=cluster, tasks=task_arns)
    for t in desc.get('tasks', []):
        # Check health/status fields; this is example logic
        health = t.get('healthStatus')
        last_status = t.get('lastStatus')
        if health and isinstance(health, str) and health.lower() == 'unhealthy' or last_status == 'STOPPED':
            task_arn = t['taskArn']
            logger.info('Stopping unhealthy task %s', task_arn)
            ecs.stop_task(cluster=cluster, task=task_arn, reason='Automated remediation from Lambda')
            return { 'status': 'stopped_task', 'task': task_arn }

    # No obvious unhealthy tasks — optionally stop one task to force replacement
    candidate = task_arns[0]
    logger.info('Stopping candidate task %s to trigger replacement', candidate)
    ecs.stop_task(cluster=cluster, task=candidate, reason='Scheduled remediation')
    return { 'status': 'stopped_task', 'task': candidate }
