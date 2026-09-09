#B
START
    // Step 1: Input Name
    OUTPUT "Enter student name:"
    INPUT name
    IF name IS EMPTY THEN
        OUTPUT "REGISTRATION NOT ACCEPTED"
        OUTPUT "-----------------------"
        OUTPUT "Student name is required."
        EXIT
    ENDIF

    // Step 2: Input Age
    OUTPUT "Please Enter Your Age:"
    INPUT age_input
    IF age_input IS NOT A NUMBER THEN
        OUTPUT "REGISTRATION NOT ACCEPTED"
        OUTPUT "-----------------------"
        OUTPUT "Age must be a number."
        EXIT
    ELSE
        CONVERT age_input TO INTEGER age
        IF age < 11 OR age > 18 THEN
            OUTPUT "REGISTRATION NOT ACCEPTED"
            OUTPUT "-----------------------"
            OUTPUT "Age must be from 11 to 18."
            EXIT
        ENDIF
    ENDIF

    // Step 3: Input Grade Level
    OUTPUT "Please Enter Your Grade Level:"
    INPUT grade_input
    IF grade_input IS NOT A NUMBER THEN
        OUTPUT "REGISTRATION NOT ACCEPTED"
        OUTPUT "-----------------------"
        OUTPUT "Invalid grade level."
        EXIT
    ELSE
        CONVERT grade_input TO INTEGER grade
        IF grade < 7 OR grade > 12 THEN
            OUTPUT "REGISTRATION NOT ACCEPTED"
            OUTPUT "-----------------------"
            OUTPUT "Invalid grade level."
            EXIT
        ENDIF
    ENDIF

    // Step 4: Input Email
    OUTPUT "Please Enter Your Email:"
    INPUT email
    IF email DOES NOT CONTAIN "@" OR email DOES NOT CONTAIN "." THEN
        OUTPUT "REGISTRATION NOT ACCEPTED"
        OUTPUT "-----------------------"
        OUTPUT "Invalid email format."
        EXIT
    ENDIF

    // Step 5: Input Registration Code
    OUTPUT "Please Enter Your Registration Code:"
    INPUT reg_code
    IF LENGTH OF reg_code IS NOT EQUAL TO 6 THEN
        OUTPUT "REGISTRATION NOT ACCEPTED"
        OUTPUT "-----------------------"
        OUTPUT "The registration code must contain exactly 6 characters."
        EXIT
    ENDIF

    // Step 6: Success Output
    OUTPUT "-----------------------"
    OUTPUT "REGISTRATION ACCEPTED"
    OUTPUT "-----------------------"
    OUTPUT "Student: " + name
    OUTPUT "Age: " + age
    OUTPUT "Grade Level: " + grade
    OUTPUT "Email: " + email
    OUTPUT "Registration Code: " + reg_code
END

