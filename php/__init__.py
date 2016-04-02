from __future__ import print_function

import sys


class PHPException(Exception):
    pass


class PHP(object):
    def __getattr__(self, name):
        import subprocess
        import json
        import tempfile

        def call_php_function(*args):
            with tempfile.NamedTemporaryFile(mode='w+t') as f:
                php_code = (
                    "<?php\n"
                    "$args = json_decode('{args}', true);\n"
                    "ob_start();\n"
                    "$result = @call_user_func_array('{function_name}', $args);\n"
                    "$buffer = ob_get_contents();\n"
                    "ob_end_clean();"
                    "if ($buffer) {{ $result = $buffer; }}\n"
                    "echo json_encode($result);"

                ).format(args=json.dumps(args).replace("'", "\\'"),
                         function_name=call_php_function.name)
                f.write(php_code)
                f.flush()
                # f.seek(0)
                # print "%s\n-------------\n%s\n\n" % (f.name, f.read())
                process = subprocess.Popen(['php', '-f', f.name], stdout=subprocess.PIPE)
                out, err = process.communicate()
                out = out.decode('utf-8')
            if err:
                raise PHPException(err)
            return json.loads(out)
        if name in ['echo', 'print']:
            return print
        call_php_function.name = name
        return call_php_function

sys.modules['php'] = PHP()
