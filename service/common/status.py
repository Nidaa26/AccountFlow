"""
HTTP Status Codes used by the Accounts service.

Defined as plain constants rather than importing them, so routes and
tests read clearly, e.g. status.HTTP_201_CREATED.
"""
HTTP_200_OK = 200
HTTP_201_CREATED = 201
HTTP_204_NO_CONTENT = 204
HTTP_400_BAD_REQUEST = 400
HTTP_404_NOT_FOUND = 404
HTTP_405_METHOD_NOT_ALLOWED = 405
HTTP_409_CONFLICT = 409
HTTP_415_UNSUPPORTED_MEDIA_TYPE = 415
HTTP_500_INTERNAL_SERVER_ERROR = 500
