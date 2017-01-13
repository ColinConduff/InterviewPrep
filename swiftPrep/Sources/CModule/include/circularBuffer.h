
typedef struct _CircularBuffer CircularBuffer;

struct _CircularBuffer
{
	int* data;
	unsigned int item_count;
	unsigned int container_size;
	unsigned int write_index;
	unsigned int read_index;
};

CircularBuffer* create_circular_buffer(unsigned int container_size);
void delete_circular_buffer(CircularBuffer* buffer);

const int circular_buffer_length(CircularBuffer* buffer);

void enqueue_circular_buffer(CircularBuffer* buffer, int item);
int dequeue_circular_buffer(CircularBuffer* buffer);

void print_circular_buffer(CircularBuffer* buffer);


static void inc_read_index(CircularBuffer *buffer);
static void inc_write_index(CircularBuffer *buffer);