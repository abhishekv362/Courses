
## Aim : Get Output like: _XYZZY53656C696E613333_

**Step 1 :** Parse the given JSON file.
**Step 2 :** Create a database.
**Step 3 :** Run the Following query -
>SELECT User.name,Course.title, Member.role FROM 
>User JOIN Member JOIN Course 
>ON User.id = Member.user_id AND Member.course_id = Course.id
>ORDER BY User.name DESC, Course.title DESC, Member.role DESC LIMIT 2;

**Step 4 :** Run this query -
>SELECT 'XYZZY' || hex(User.name || Course.title || Member.role ) AS X FROM 
>User JOIN Member JOIN Course 
>ON User.id = Member.user_id AND Member.course_id = Course.id
>ORDER BY X LIMIT 1;

**Step 4 :** Hurraaah Objective Achieved.

###         **My Output -> _XYZZY4161697661736933363430_**
