import json
import boto3
import uuid


transcribe = boto3.client('transcribe')

def lambda_handler(event, context):
    print("Hello guys I am Pappu Sanodiya....")
    
    filename = event['Records'][0]['s3']['object']['key']
    bucketname = event['Records'][0]['s3']['bucket']['name']

    url = "s3://" + bucketname + "/" + filename

    myuuid = uuid.uuid1().int
    print(event, url, bucketname)
    response = transcribe.start_transcription_job(

                    TranscriptionJobName="myaudiojob" + "-" + str(myuuid), 
                    LanguageCode='en-US',
                    MediaFormat='mp3',
                    Media={
                        'MediaFileUri': url,
                            },
                    OutputBucketName="myoutputbucket1234",
                    
                    OutputKey="myaudiojob" + "-" + str(myuuid) + ".json"
                    )
    

    print(response)
