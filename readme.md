### difference between jsonresponse and httpResponse
    jsonresponse is a response object that is used to send json data to the client.
    httpresponse is a response object that is used to send html data to the client.

### drf Model serializer
    serializer is used to serialize the data from the model into json format.

### object.first()
    object.first() is used to get the first object from the queryset.

    ```
    object.first()
    
    ```

### object.all()
    object.all() is used to get all the objects from the queryset.

### object.count()
    object.count() is used to get the count of the objects from the queryset.

### object.filter()
    object.filter() is used to get the filtered objects from the queryset.
    if there is no record in the database then it will return empty queryset.
    it will show multiple records against one id.

    show records whose id less then 20

    ```
    object.filter(id__lte=20)
    
    ```

    show records whose id greater then 20

    ```
    object.filter(id__gte=20)
    
    ```

### object.exclude()
    object.exclude() is used to get the filtered objects from the queryset.

### object.get()
    object.get() is used to get the object from the queryset.
    it will show exeception if there is no record in the database.
    it will show single record against one id.
    if there are multiple records against one id then it will show exception.

### Field lookups
    Field lookups are how you specify the meat of an SQL WHERE clause. They’re specified as keyword arguments to the QuerySet methods filter(), exclude() and get().

    Basic lookups keyword arguments take the form ** field__lookuptype=value **. (That’s a double-underscore). For example:

    Entry.objects.filter(pub_date__lte='2006-01-01')

    translates (roughly) into the following SQL:

    SELECT * FROM blog_entry WHERE pub_date <= '2006-01-01';    
