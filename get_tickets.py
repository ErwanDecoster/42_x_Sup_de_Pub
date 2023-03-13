import requests

url = 'https://dzwnevyguwlsxzrthfrt.supabase.co/rest/v1/Tickets?select=created_at'

token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImR6d25ldnlndXdsc3h6cnRoZnJ0Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2Nzg3MTY4MzIsImV4cCI6MTk5NDI5MjgzMn0.P34a3RgwniQJ_GeKKp92GkvKsnzN9peRJ_loUZoYetk'


a = requests.get(url, headers={'apikey': token}).json()
print(a)
