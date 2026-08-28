import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    """Example Lambda that tags an EC2 instance with IncidentStatus=Investigate.

    Expects the instance ID to be present in the triggering EventBridge event
    under detail.instance-id or detail.instanceId. Adjust parsing as needed.
    """
    logger.info('Received event: %s', event)
    detail = event.get('detail', {})
    instance_id = detail.get('instance-id') or detail.get('instanceId') or detail.get('InstanceId')
    if not instance_id:
        logger.error('No instance ID found in event')
        return { 'status': 'error', 'reason': 'no instance id' }

    try:
        ec2.create_tags(Resources=[instance_id], Tags=[{'Key': 'IncidentStatus', 'Value': 'Investigate'}])
        logger.info('Tagged instance %s with IncidentStatus=Investigate', instance_id)
        return { 'status': 'tagged', 'instance': instance_id }
    except Exception as e:
        logger.exception('Failed to tag instance')
        return { 'status': 'error', 'reason': str(e) }
