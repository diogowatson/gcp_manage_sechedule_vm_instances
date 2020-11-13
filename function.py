from pprint import pprint
from googleapiclient import discovery
from oauth2client.client import GoogleCredentials


def start_instance(project, zone, instance):
    """start an vm instance
       project (string) -> id of the project
       zone (string) -> zone of the computing instance
       instance (string) -> name of the instance"""
       
    credentials = GoogleCredentials.get_application_default()
    service = discovery.build('compute', 'v1', credentials=credentials)
    request = service.instances().start(project=project, zone=zone, instance=instance)
    response = request.execute()
    pprint(response)


def stop_instance(project, zone, instance):
       """stop an vm instance
       project (string) -> id of the project
       zone (string) -> zone of the computing instance
       instance (string) -> name of the instance"""
       
    credentials = GoogleCredentials.get_application_default()
    service = discovery.build('compute', 'v1', credentials=credentials)
    request = service.instances().stop(project=project, zone=zone, instance=instance)
    response = request.execute()
    pprint(response)


def start_event(event, context):
    """Triggera message from a Cloud Pub/Sub topic.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.

    message format (JSON):
	    {
		 'project':'<project-id>',
		 'zone':'<instance zone>',
		 'instance':<instace name>'
		 'action':'<start or stop>'
		 }
    """
    credentials = GoogleCredentials.get_application_default()

    service = discovery.build('compute', 'v1', credentials=credentials)

    # project id for the request
    project = event['project']

    # zone for the project
    zone = event['zone']

    # name of the instance
    instance = event['instance']

    # action to be executed
    action = event['action']

    if action == 'start':
        start_instance(project, zone, instance)
    elif action == 'stop':
        stop_instance(project, zone, instance)
    else:
        pprint("no valid arguments")

    pprint("function executed")
