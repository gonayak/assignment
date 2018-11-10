import requests
import json

test_url = 'https://dev.rackspace.example.com/widgets/'

def get(url):
	# get all widgets
	resp = requests.get ( url)
	assert resp.status_code == requests.codes.ok, 'Bad status returned {}, put request headers {}, content {}'.format (
		resp.status_code, resp.headers, resp.content )
	print (resp.json ())

#GET: Get all widgets
get ( test_url )


def post_it():
	post_url = test_url
	json_input={"widget_name": "Test Widget", "description": "Description"}
	request_json = json.loads ( json_input )
	print(request_json)

	resp = requests.post ( post_url, request_json )

	assert resp.status_code == requests.codes.created, 'Bad status returned {}'.format ( resp.status_code )
	print('Response:\n{}'.format ( resp.content ))
	# validate the post is success
	response = resp.json ()
	if (response["widget_name"] == "Test Widget"):
		print("post success")


post_it ()


# 3.https://dev.rackspace.example.com/widgets/{widget_id}

def get_response(widget_id):
	resp = requests.get ( test_url + widget_id )
	assert resp.status_code == requests.codes.ok, 'Bad status returned {}, put request headers {}, content {}'.format (
		resp.status_code, resp.headers, resp.content )
	print (resp.json ())

#call get response with the widget_id as 1
get(1)


# 4.PUT: Update an existing widget

def put_it(widget_id):
	post_url = test_url + widget_id

	json_input =   {"description": "A new description"}
	request_json = json.loads ( json_input )
	print(request_json)


	resp = requests.put ( post_url, data=request_json )
	assert resp.status_code == requests.codes.no_content, 'Bad status returned {}, put request headers {}, content {}'.format (
		resp.status_code, resp.headers, resp.content )
	print(resp.json ())
	if (resp.json["description"]) == "A new description":
		print("the update was succsess")




def delete(widget_id):
	resp = requests.delete ( test_url, widget_id )
	assert resp.status_code == requests.codes.no_content, 'Bad status returned {}, put request headers {}, content {}'.format (
		resp.status_code, resp.headers, resp.content )
	print('Response:\n{}'.format ( resp.text ))

#call delete with the widget_id as 1
delete(1)
