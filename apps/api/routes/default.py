from apps.api.app import APP_NAME, bp


@bp.route("/", methods=["GET"])
def index():
    """Index of application
    ---
    responses:
      '200':
        description: Index
        content:
          application/json:
            schema:
              application: string
    """
    return dict(application=f"{APP_NAME} API"), 200
