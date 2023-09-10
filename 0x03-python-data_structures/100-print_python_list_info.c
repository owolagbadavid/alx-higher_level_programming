#include <stdio.h>
#include <Python.h>


/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: pointer to PyObject
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	int i;
	PyObject *item;

	printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < PyList_Size(p); i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
