from rest_framework.views import APIView
from django.db import connection
from .HelpController import HelpController
from django.http import JsonResponse, HttpResponse
import json


class FrameController(APIView):

    @classmethod
    def frames(cls, request):
        url_data = request.build_absolute_uri().split("?")
        page = request.GET.get('page')
        page_size = 12
        offset = (int(page) - 1) * page_size
        cursor = connection.cursor()
        sql_count = """Select count(f.id) from frames f where f.is_active = 0"""
        cursor.execute(sql_count, [])
        post_count = cursor.fetchone()
        sql = """Select * from frames f where f.is_active = 0 order by f.updated_at desc LIMIT %s OFFSET %s"""
        cursor.execute(sql, [page_size, offset])
        rows = cursor.fetchall()
        result = []
        keys = (
            'id',
            'frame_sku',
            'thumb',
            'is_text',
            'text_pos',
        )

        for row in rows:
            print(row[0])
            result.append(dict(zip(keys, row)))

        response = {
            "links": HelpController.get_page_links(
                url_data=url_data,
                offset=offset,
                page_size=page_size,
                page=page,
                array_count=post_count
            ),
            "count": post_count[0],
            "results": result
        }

        json_data = json.dumps(response, default=str)
        return HttpResponse(json_data, content_type="application/json")
