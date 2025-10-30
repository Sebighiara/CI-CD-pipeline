import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.main import app

def test_home_route():
	client = app.test_client()
	response = client.get('/')
	assert response.status_code == 200
	assert b"Hello, DevOps world!" in response.data

