import sys
import io, os

class last_lines(object):
  def __call__(self, file_name, buffer_size=io.DEFAULT_BUFFER_SIZE):
    with open(file_name, 'rb') as file_read:
        #go to the end of the file using read byte mode
        file_read.seek(0, os.SEEK_END)
        position = file_read.tell()

        #fill buffer with value read until find end of line or get to size of buffer
        buffer = bytearray()
        while position >= 0:
            file_read.seek(position)
            value_read = file_read.read(1)
            position -= 1

            if len(buffer) == buffer_size - 1:
                reversed_buffer = buffer[::-1]
                reversed_buffer.extend(b'\n')
                yield reversed_buffer.decode('utf8', errors='replace')
                buffer = bytearray()
                buffer.extend(value_read)

            elif value_read == b'\n':
                reversed_buffer = buffer[::-1]
                reversed_buffer.extend(value_read)
                yield reversed_buffer.decode('utf8', errors='replace')
                buffer = bytearray()

            else:
                buffer.extend(value_read)
        
        #if got to the end of file and buffer is not empty
        if len(buffer) > 0:
            reversed_buffer = buffer[::-1]
            reversed_buffer.extend(b'\n')
            yield reversed_buffer.decode('utf8', errors='replace')

sys.modules[__name__] = last_lines()
