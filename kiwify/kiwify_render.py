from rest_framework.renderers import BaseRenderer
from rest_framework.renderers import JSONRenderer

from rest_framework.utils.serializer_helpers import ReturnDict


class KiwifyRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        response = {"success": True, "errors": None, "data": data}

        if not data:
            response["success"] = False
            response["errors"] = "No data found"

        if "detail" in data:
            response["success"] = False
            response["errors"] = data["detail"]

        if "errors" in data:
            response["success"] = False
            response["errors"] = data["errors"]
        
        if renderer_context:
            response_status_code = renderer_context.get('response').status_code
            if response_status_code != 200:
                response["success"] = False
                response["errors"] = data
                response["data"] = None

        return super(KiwifyRenderer, self).render(response, accepted_media_type, renderer_context)
