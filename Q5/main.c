//
//  main.c
//  a1.comp348
//
//  Created by Maria Ghobrial on 2022-05-11.
//

#include <stdio.h>
#include <stdlib.h>
#include "AGGREGATE.H"

typedef enum { //type
    ATOM,
    LIST
} type;

typedef char atom;
struct _listnode;

typedef struct { //element
    type type; //atom or list
    union {
        atom a;
        struct _listnode* listptr;
    };
} element;

typedef struct _listnode {
    type type;
    element el;
    struct _listnode* next;
} *list;

const element NIL = { .type = LIST, .listptr = NULL };

element aasel(atom a);
element lasel(list l);
element car(element e);
list cdr(element e);
list cddr(element e);
list cons(element e, list l);
list append(list l1, list l2);
void lfreer(list l);
void printlist(element e);
void insert(list* root, element item);


int main() {
//    float (*aggregates[5])(float arr[], int) = {min, max, sum, avg, pseudo_avg};
//
//       float arr1[5]={2.4, 5.6, 2.2, 3.4,8.9};
//       float arr2[10]={1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0};
//       // iterates through the array of functions and calls each function on the two sample arrays you defined
//       for (int i=0; i<5 ;i++){
//           aggregates[i] (arr1, 5);
//           aggregates[i] (arr2,10);
//
//       }
    
    list l = (list)malloc(sizeof(struct _listnode));
        element l2;
        l2.listptr = l;

        //element * l2 = &l;
        l2.type = LIST;
        element e;
        e.a = 'e';
        e.type = ATOM;
        element d;
        d.a = 'd';
        d.type = ATOM;

        cons(e, l);
        cons(d, l);

        //printf("hello");
        //printf("%c", e.a);
       //printf("hello");
       // printlist(e);
        //printlist(d);
        printlist(l2);
    

}

element aasel(atom a) { //atom -> type char
    element content;
    content.type = ATOM; //setting element to be type atom
    content.a = a;
    return content;

}

element lasel(list l) {
    element data;
    data.type = LIST; //setting element to be type list
    data.listptr = l;
    return data; //returns the content as a LIST
}

element car(element e) {
    if (e.type != LIST) {
        return NIL;
    }
    return e.listptr->el; //e.next points to next node //SUPPOSED TO POINT TO HEAD
}

list cdr(element e) {
    if (e.type != LIST || e.listptr == NULL) { //if e is not a LIST or if e.next == null
        return NULL;
    }

    return e.listptr->next; //returns the tail of the list
}

list cddr(element e) {
    return cdr(lasel(cdr(e)));
}

list cons(element e, list l) {
    list first_ele = (list)malloc(sizeof(struct _listnode));

    first_ele->el = car(e);
    first_ele->next = l;
    return first_ele;
}

list append(list l1, list l2) {
    list newList = NULL;

    //list it = l1;
    while (l1 != NULL) {
        insert(&newList, l1->el);
        l1 = l1->next;
    }

    // list it2 = l2;
    while (l2 != NULL) {
        insert(&newList, l2->el);
        l2 = l2->next;
    }

    return newList;
}
void freeList(list l1) {
    // list it = l;

    while (l1 != NULL) {
        if (l1->el.type == LIST) {
            freeList(l1->el.listptr);
        }

        list temp = l1->next;
        free((void*)l1);
        l1 = temp;
    }
}
void printlist(element e) {
    if (e.type == LIST && e.listptr == NULL) { //if its an empty list
        printf(" NIL ");
        return;
    }
    else if (e.type == ATOM) {
        printf(" %c ", e.a); //print the data
    }
    else if (e.type== LIST){
        list current = e.listptr;//current=e.next
        printf(" (");
        while (current != NULL) {
            printlist(current->el); //print next node
            current = current->next; //moves pointer to next node
        }
        printf(") ");
    }
}

void insert(list* root, element item) {
    list temp = (list)malloc(sizeof(struct _listnode));
    list ptr;
    temp->el = item;
    temp->next = NULL;

    if (*root == NULL)
        *root = temp;
    else {
        ptr = *root;
        while (ptr->next != NULL)
            ptr = ptr->next;
        ptr->next = temp;
    }
}

