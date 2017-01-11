
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#include "include/arrayList.h"

ArrayList *create_array() {
    const int initial_container_size = 16;

    ArrayList *array = (ArrayList *) malloc(sizeof(ArrayList));

    if(array == NULL) { return NULL; }

    array->container_size = initial_container_size;
    array->length = 0;
    array->data = malloc(initial_container_size * sizeof(int));

    if(array->data == NULL) {
        free(array);
        return NULL;
    }

    return array;
}

void delete_array(ArrayList *array) {
    if(array != NULL) {
        free(array->data);
        free(array);
    }
}

int array_length(ArrayList *array) {
    return array->length;
}

static void expand(ArrayList *array) {
    int *data;
    unsigned int new_container_size = array->container_size * 2;

    data = realloc(array->data, sizeof(int) * new_container_size);

    if(data != NULL) {
        array->data = data;
        array->container_size = new_container_size;
    }
}

static void contract(ArrayList *array) {
    int *data;
    unsigned int new_container_size = array->container_size / 2;

    data = realloc(array->data, sizeof(int) * new_container_size);

    if(data != NULL) {
        array->data = data;
        array->container_size = new_container_size;
    }
}

void array_insert(ArrayList *array, unsigned int index, int data) {

    // Time: Amortized O(n)

    if(index > array->length) { return; }

    if(array->length + 1 > array->container_size) {
        expand(array);
        if(array->data == NULL) { return; }
    }

    memmove(&array->data[index + 1],
            &array->data[index],
            (array->length - index) * sizeof(int));

    array->data[index] = data;
    ++(array->length);

    return;
}

void array_append(ArrayList *array, int data) {
    // Time: Amortized O(1)
    array_insert(array, array->length, data);
}

int array_pop(ArrayList *array) {

    if(array->length == 0) { return 0; }
    
    int last_item_index;
    int last_item;

    last_item_index = array->length - 1;
    last_item = array->data[last_item_index];
    --(array->length);

    if(array->length < array->container_size / 2) {
        contract(array);
    }

    return last_item;
}

void array_print(ArrayList *array) {
    int length = array->length;
    
    char str[length];
    int i=0;
    int index = 0;
    for (i=0; i<length; i++) {
       index += snprintf(&str[index], length, "%d ", array->data[i]);
    }

    printf("%s\n", str);
}

