# Student-Search
This script that allows you to search for a student in a JSON file by their fullname,Birthday,Address,CIN,CEN,Phone and Email.

## Setup
``` 
https://github.com/Over-k/Student-Search.git
pip install -r requirements.txt
python app.py
```
## Example
``` 
  search("fullname", "James Brown", 10)
```
- `fullname` : Search by key also u can change to Birthday,Address,CIN,CEN,Phone and Email.
- `James Brown` : The value you are looking for
- `10`: Max student to display

### Output : 

| cin       | cne        | nationality | fullname    | date_birthday | gender | address      | code_postal | phone      | email           | father     | mother     |
|-----------|------------|-------------|-------------|----------------|--------|--------------|-------------|------------|----------------|------------|------------|
| EE555555  | P567890123 | 350         | James Brown | 05/17/1999    | M      | 654 Oak St   | 43210       | 567-890-1234 | james@example.com | Mike Brown | Sarah Brown |


## Demo
[To see a demonstration.](https://4demobyoverk.pythonanywhere.com/)
> :warning: In the demo contains real information. ``~500K students``
