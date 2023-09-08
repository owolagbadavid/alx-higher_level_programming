#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to head of list
 * Return: 0 if not palindrome, 1 if it is
 */
int is_palindrome(listint_t **head)
{
    listint_t *tmp = *head;
    int i = 0, j = 0, arr[10000];

    if (!head || !*head)
        return (1);
    while (tmp)
    {
        arr[i] = tmp->n;
        tmp = tmp->next;
        i++;
    }
    i--;
    while (j < i)
    {
        if (arr[j] != arr[i])
            return (0);
        j++;
        i--;
    }
    return (1);
}