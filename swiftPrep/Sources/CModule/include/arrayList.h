
typedef struct _CArrayList ArrayList;

struct _CArrayList {
	int *data;
	unsigned int length;
	unsigned int container_size;
};

ArrayList *create_array();
void delete_array(ArrayList *array);

int array_length(ArrayList *array);

void array_insert(ArrayList *array, unsigned int index, int data);
void array_append(ArrayList *array, int data);

int array_pop(ArrayList *array);

void array_print(ArrayList *array);
