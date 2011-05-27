# curl -H "Accept: application/json" -X GET http://127.0.0.1:8000/
# curl -H "Accept: application/json" -X POST http://127.0.0.1:8000/ --data "title=tt&text=body"

#curl -X GET http://127.0.0.1:8000/
curl -X POST http://127.0.0.1:8000/ --data "title=tt&text=body"
