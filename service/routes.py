

"""
Account Service

This service implements a REST API that lets you Create, Read, Update,
Delete, and List Accounts.
"""
from flask import jsonify, request, url_for, abort
from service.models import Account
from service.common import status
from service import app


############################################################
# HEALTH ENDPOINT
############################################################
@app.route("/health")
def health():
    """Let them know our heart is still beating"""
    return jsonify(status="OK"), status.HTTP_200_OK


############################################################
# GET INDEX
############################################################
@app.route("/")
def index():
    """Root URL response with basic service info"""
    return (
        jsonify(
            name="Account REST API Service",
            version="1.0",
            paths=url_for("list_accounts", _external=True),
        ),
        status.HTTP_200_OK,
    )


############################################################
# CREATE A NEW ACCOUNT
############################################################
@app.route("/accounts", methods=["POST"])
def create_accounts():
    """Creates an Account and stores it in the database"""
    app.logger.info("Request to create an Account")
    check_content_type("application/json")

    account = Account()
    account.deserialize(request.get_json())
    account.create()

    message = account.serialize()
    location_url = url_for("read_account", account_id=account.id, _external=True)

    return jsonify(message), status.HTTP_201_CREATED, {"Location": location_url}


############################################################
# LIST ALL ACCOUNTS
############################################################
@app.route("/accounts", methods=["GET"])
def list_accounts():
    """Returns a list of all the Accounts"""
    app.logger.info("Request to list Accounts")
    accounts = Account.all()
    account_list = [account.serialize() for account in accounts]
    return jsonify(account_list), status.HTTP_200_OK


############################################################
# READ AN ACCOUNT
############################################################
@app.route("/accounts/<int:account_id>", methods=["GET"])
def read_account(account_id):
    """Reads a single Account by its id"""
    app.logger.info("Request to read an Account with id: %s", account_id)
    account = Account.find(account_id)
    if not account:
        abort(
            status.HTTP_404_NOT_FOUND,
            f"Account with id [{account_id}] could not be found.",
        )
    return jsonify(account.serialize()), status.HTTP_200_OK


############################################################
# UPDATE AN EXISTING ACCOUNT
############################################################
@app.route("/accounts/<int:account_id>", methods=["PUT"])
def update_accounts(account_id):
    """Updates an existing Account"""
    app.logger.info("Request to update an Account with id: %s", account_id)
    account = Account.find(account_id)
    if not account:
        abort(
            status.HTTP_404_NOT_FOUND,
            f"Account with id [{account_id}] could not be found.",
        )
    account.deserialize(request.get_json())
    account.id = account_id
    account.update()
    return jsonify(account.serialize()), status.HTTP_200_OK


############################################################
# DELETE AN ACCOUNT
############################################################
@app.route("/accounts/<int:account_id>", methods=["DELETE"])
def delete_accounts(account_id):
    """Deletes an Account from the database"""
    app.logger.info("Request to delete an Account with id: %s", account_id)
    account = Account.find(account_id)
    if account:
        account.delete()
    return "", status.HTTP_204_NO_CONTENT


############################################################
# UTILITY FUNCTIONS
############################################################
def check_content_type(content_type):
    """Checks that the media type is correct"""
    if "Content-Type" not in request.headers:
        abort(
            status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            f"Content-Type must be {content_type}",
        )
    if request.headers["Content-Type"] != content_type:
        abort(
            status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            f"Content-Type must be {content_type}",
        )
