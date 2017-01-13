
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#include "include/circularBuffer.h"

CircularBuffer* create_circular_buffer(unsigned int container_size) 
{
	CircularBuffer* buffer;

	buffer = (CircularBuffer*) malloc(sizeof(CircularBuffer));

	if (buffer == NULL) { return NULL; }

	buffer->container_size = container_size;
    buffer->item_count = 0;
    buffer->data = malloc(container_size * sizeof(int));
    buffer->write_index = 0;
    buffer->read_index = 0;

    if (buffer->data == NULL) {
        free(buffer);
        return NULL;
    }

    return buffer;
}

void delete_circular_buffer(CircularBuffer* buffer)
{
	if (buffer != NULL) 
	{ 
		free(buffer->data); 
		free(buffer);
	}
}

const int circular_buffer_length(CircularBuffer* buffer)
{
	return (buffer == NULL) ? 0 : buffer->item_count;
}

/**
Enqueue a new element in the buffer.

Write and read indices should always be less than the container size.

Valid data exists between (read_index and write_index) % container_size.
Must watch for stale/invalid data being accessed.
*/
void enqueue_circular_buffer(CircularBuffer* buffer, int item)
{
	if (buffer == NULL) { return; }

	buffer->data[buffer->write_index] = item;

	inc_write_index(buffer);
	++(buffer->item_count);
}

/**
Pop an item off of the queue.

Need to figure out a better way to return errors.
Maybe return struct that represents optional values.
*/
int dequeue_circular_buffer(CircularBuffer* buffer)
{
	int item;

	if (buffer == NULL) { return -1; }
	if (buffer->item_count == 0) { return -1; }

	item = buffer->data[buffer->read_index];

	inc_read_index(buffer);
	--(buffer->item_count);

	return item;
}

void print_circular_buffer(CircularBuffer* buffer) 
{
    const int c_str_size = buffer->item_count * 2; // size = items + spaces
    char str[c_str_size];
    int i;
    int c_str_index;

    c_str_index = 0;

    for (i = buffer->read_index; 
    	 i < buffer->container_size && i < buffer->write_index; 
    	 i++) 
    {
       c_str_index += snprintf(&str[c_str_index], c_str_size, "%d ", buffer->data[i]);
    }

    // Wrap around to the beginning if necessary
    if (i != buffer->write_index && i == buffer->container_size) 
    {
	    for (i = 0; i < buffer->write_index; i++) 
	    {
	       c_str_index += snprintf(&str[c_str_index], c_str_size, "%d ", buffer->data[i]);
	    }
	}

    printf("%s\n", str);
}

/**
Increments the read_index.
Sets it to 0 if it reaches the end of the container.
*/
static void inc_read_index(CircularBuffer *buffer) 
{
	if (buffer == NULL) { return; }
	
	++(buffer->read_index);

	if (buffer->read_index > buffer->container_size) {
		buffer->read_index = 0;
	}
}

/**
Increments the write_index.
Sets it to 0 if it reaches the end of the container.
*/
static void inc_write_index(CircularBuffer *buffer) 
{
	if (buffer == NULL) { return; }
	
	++(buffer->write_index);

	if (buffer->write_index > buffer->container_size) {
		buffer->write_index = 0;
	}
}