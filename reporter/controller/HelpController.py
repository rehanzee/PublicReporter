

class HelpController:

    @classmethod
    def get_page_links(cls, url_data, offset, page_size, page, array_count):
        next_url = None
        if page_size + offset < array_count[0]:
            next_url = url_data[0] + "?page=" + str(int(page) + 1)

        prev_url = None
        if offset > 0:
            prev_url = url_data[0] + "?page=" + str(int(page) - 1)

        return {
            "next": next_url,
            "previous": prev_url
        }