# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.


import flask


def get_routing_list(app):
    """Make a sumple list of routing rules.

    :param app: Flask application
    :returns: list of routes
    """
    routes = []
    for route in app.url_map.iter_rules():
        routes.append({"uri": route.rule,
                       "methods": sorted(list(route.methods)),
                       "endpoint": route.endpoint})
    routes.sort(key=lambda d: d["uri"])
    return routes


def add_routing_map(app,
                    html_uri="/map.html",
                    json_uri="/map.json",
                    html_endpoint="routing_map_html",
                    json_endpoint="routing_map_json"):
    """Register blueprint with routing map pages.

    :param app: Flask application
    :param html_uri: str URI for HTML page,
                     None if disabled
    :param json_uri: str URI for JSON page,
                     None if disabled
    :param html_endpoint: str endpoint for HTML page
    :param json_endpoint: str endpoint for JSON page
    :returns: Flask application
    """
    bp = flask.Blueprint("routing_map", __name__,
                         template_folder="templates")
    routes = get_routing_list(app)
    if html_uri:
        bp.route(html_uri, endpoint=html_endpoint)(
            lambda: flask.render_template("routing_map.html",
                                          routes=routes,
                                          json_uri=json_uri))
    if json_uri:
        bp.route(json_uri, endpoint=json_endpoint)(
            lambda: flask.jsonify(routes))
    app.register_blueprint(bp)
    return app
