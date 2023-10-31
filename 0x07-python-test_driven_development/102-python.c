#include "Python.h"

/**
 * print_python_string - Print information about a Python string.
 * @p: PyObject string pointer
 */
void print_python_string(PyObject *p)
{
	long int length;

	fflush(stdout);

	printf("[.] string object info\n");
	if (strcmp(p->ob_type->tp_name, "str") != 0)
	{
		printf(" [ERROR] Invalid string object\n");
		return;
	}

	length = ((PyASCIIObject *)(p))->length;

	if (PyUnicode_IS_COMPACT_ASCII(P))
		printf("  type: compact ascii\n");
	else
		printf(" type: compact unicode object\n");
	printf(" length: %ld\n", length);
	printf(" value: %ls\n", PyUnicode_AswideCharString(p, &length));
}
