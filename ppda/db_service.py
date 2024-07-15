from frappeclient import FrappeClient
import config


class DBService:
    """
    A service class to interact with the Frappe server.
    Usage:
    ```
    conn = DBService('https://example.com')
    conn.login('admin', 'admin')

    conn.get_list('Customer')
    conn.get_doc('Customer', 'Example Co')
    conn.get_value('Customer', 'customer_name', {'name': 'Example Co'})

    conn.insert({
        "doctype": "Customer",
        "customer_name": "Example Co",
        "customer_type": "Company",
        "website": "example.net"
    })

    doc = conn.get_doc('Customer', 'Example Co')
    doc['phone'] = '000000000'
    conn.update(doc)

    conn.delete('Customer', 'Example Co')
    """

    client = FrappeClient(config.BASE_URL)

    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(DBService, cls).__new__(cls)
        return cls.instance

    def login(self, username, password):
        self.client.login(username, password)

    def get_list(
        self,
        doctype,
        fields=["*"],
        filters=None,
        limit_start=0,
        limit_page_length=20,
        order_by=None,
    ):
        """
        Get a list of documents from the server

        Arguments:
        - doctype
        - fields: List of fields to fetch
        - filters: Dict of filters
        - limit_start: Start at row ID (default 0)
        - limit_page_length: Page length
        - order_by: sort key and order (default is modified desc)

        Example of filters:
        { "user_type": ("!=", "System User") }
        { "creation": (">", "2020-01-01") }
        { "name": "test@example.com" }
        """
        return self.client.get_list(
            doctype, fields, filters, limit_start, limit_page_length, order_by
        )

    def get_doc(self, doctype, name):
        """
        Get a document from the server

        Arguments:
        - doctype
        - name: Document name
        """
        return self.client.get_doc(doctype, name)

    def get_value(self, doctype, fieldname, filters):
        """
        Get a value from the server.

        Arguments:
        - doctype
        - fieldname: Field name
        - filters: Dict of filters
        """
        return self.client.get_value(doctype, fieldname, filters)

    def insert(self, doc):
        """
        Insert a document into the server.

        `doc` is a dict of the document to insert including the doctype. Example:
        {
            "doctype": "Customer",
            "customer_name": "Example Co",
            "customer_type": "Company",
            "website": "example.net"
        }
        """
        return self.client.insert(doc)

    def insert_many(self, docs):
        """
        Insert multiple documents into the server.

        `docs` is a list of dicts of the documents to insert including the doctype. Example:
        [
            {
                "doctype": "Customer",
                "customer_name": "Example Co",
                "customer_type": "Company",
                "website": "example.net"
            },
            {
                "doctype": "Customer",
                "customer_name": "Example Co 2",
                "customer_type": "Company",
                "website": "example.net"
            }
        ]
        """
        return self.client.insert_many(docs)

    def update(self, doc):
        """
        Update a document on the server.

        `doc` is a dict of the document (JSON) to update including the doctype and name. Example:
        {
            "doctype": "Customer",
            "name": "Example Co",
            "customer_name": "Example Company",
            "website": "example.com"
        }

        Usage:
        ```
        doc = conn.get_doc('Customer', 'Example Co')
        doc['phone'] = '000000000'
        conn.update(doc)
        ```
        """
        return self.client.update(doc)

    def update_many(self, docs):
        """
        Update multiple documents on the server.

        `docs` is a list of dicts of the documents (JSON) to update including the doctype and name. Example:
        [
            {
                "doctype": "Customer",
                "name": "Example Co",
                "customer_name": "Example Company",
                "website": "example.com"
            },
            {
                "doctype": "Customer",
                "name": "Example Co 2",
                "customer_name": "Example Company 2",
                "website": "example.com"
            }
        ]
        """
        return self.client.bulk_update(docs)

    def delete(self, doctype, name):
        """
        Delete a document from the server.

        Arguments:
        - doctype
        - name: Document name
        """
        return self.client.delete(doctype, name)

    def get_api(self, method, params={}):
        """
        Call a custom API method on the server.

        Arguments:
        - method: API method name
        - params: Dict of parameters
        """
        return self.client.get_api(method, params)

    def post_api(self, method, params={}):
        """
        Call a custom API method on the server.

        Arguments:
        - method: API method name
        - params: Dict of parameters
        """
        return self.client.post_api(method, params)
