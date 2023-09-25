#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdio.h>


/**
 * print_python_bytes - prints info about python bytes
 * @p: pointer to PyObject
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *str;

	fflush(stdout);
	printf("[.] bytes object info\n");
	if (!PyBytes_CheckExact(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = PyBytes_Size(p);
	str = ((PyBytesObject *)p)->ob_sval;
	printf("  size: %zd\n", size);
	printf("  trying string: %s\n", str);
	if (size < 10)
		printf("  first %ld bytes:", size + 1);
	else
		printf("  first 10 bytes:");
	for (i = 0; i <= size && i < 10; i++)
		printf(" %02hhx", str[i]);
	printf("\n");
}


/**
 * print_python_float - prints info about python float
 * @p: pointer to PyObject
 */
void print_python_float(PyObject *p)
{
	char *str;
	double d;

	fflush(stdout);
	printf("[.] float object info\n");
	if (!PyFloat_CheckExact(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	d = ((PyFloatObject *)p)->ob_fval;
	str = PyOS_double_to_string(d, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", str);
}

/**
 * print_python_list - prints info about python lists
 * @p: pointer to PyObject
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *item;

	fflush(stdout);
	printf("[*] Python list info\n");
	if (!PyList_CheckExact(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	size = PyList_GET_SIZE(p);
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < size; i++)
	{
		item = ((PyListObject *)p)->ob_item[i];
		printf("Element %ld: %s\n", i, item->ob_type->tp_name);
		if (PyBytes_Check(item))
			print_python_bytes(item);
		else if (PyFloat_Check(item))
			print_python_float(item);
	}
}
