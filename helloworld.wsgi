def application(environ, start_response):
    status = '200 OK'
    output = b'Hello World testing cicd pipeline full phase final final testing\n'
    response_headers = [('Content-type', 'text/plain'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)
    return [output]
