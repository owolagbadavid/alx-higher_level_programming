#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdio.h>

/**
 * print_python_string - Prints information about Python strings.
 * @p: A PyObject string object.
 */
void print_python_string(PyObject *p)
{
    Py_ssize_t len;
    wchar_t *str;

    printf("[.] string object info\n");
    if (!PyUnicode_Check(p))
    {
        printf("  [ERROR] Invalid String Object\n");
        return;
    }
    if (PyUnicode_IS_COMPACT_ASCII(p))
        printf("  type: compact ascii\n");
    else
        printf("  type: compact unicode object\n");
    len = PyUnicode_GET_LENGTH(p);
    printf("  length: %ld\n", len);
    str = PyUnicode_AsWideCharString(p, &len);
    printf("  value: %ls\n", str);
}
