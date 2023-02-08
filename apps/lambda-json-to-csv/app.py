from libs.s3_client import s3_client
import os, csv, json


def handler(event, context):
  try:
    file_content = json.loads(event['body'])
    
    with open('/tmp/data.json', 'w') as f:
      json.dump(file_content, f)
    
    with open('/tmp/data.json', 'r') as f:
      csv_file = csv.writer(f)
    
    
    header = file_content[0].keys()
    csv_data = [header] + [[row[key] for key in header] for row in file_content]

    with open('/tmp/dump.csv', 'w') as f:
      _csv = csv.writer(f)
      _csv.writerows(csv_data)
  
    # s3_client().put_object(
    #   Bucket=os.environ.get('BUCKET_NAME'),
    #   Key=os.environ.get('CSV_FILE_NAME'),
    #   Body=json_data
    # )

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": "Job completed"
    }
  except Exception as e:
    print(e)
    return {
      "statusCode": 500,
      "headers": {
          "Content-Type": "text/plain"
      },
      "body": "Something went wrong"
    }
