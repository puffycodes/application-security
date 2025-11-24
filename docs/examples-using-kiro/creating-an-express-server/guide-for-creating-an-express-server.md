# Creating A Simple Express Server

## Instructions

### Setting Up

Create a working folder ```express-server``` and cd to the working folder.

```
mkdir express-server
cd express-server
```

In the working folder, create a subfolder docs.
```
mkdir docs
```

Create a file features.md with the following content in the docs folder.

```
# Sample Express Server

## Features

1. Have a home page that says "Hello. Welcome to The Home Page." and a link 'submit message' that will link to the submission page.
1. Submission page will ask user for 'email' and 'message' and have a 'Submit' button.
1. The 'Submit' button will send the email and message to the server. In return, the user will get a page showing the email and the message. The page will also have a link back to the Submission page.

```

### Generate source code and test code with Kiro

Start Kiro.

```
kiro-cli
```

Generate the source code using Kiro.

```
Generate the source code according to the specification in docs/features.md. Place the source code in the folder src/.
```

Set up the folder for running  the server.
```
Set up the source code folder for running the server.
```

Generate some test code for the server.
```
Generate test code for the server.
```

Run the test.
```
Run the test and check if the test passed.
```

Modify the test code by changing 'Welcome to The Home Page' to 'Welcome to My Home Page' and do the above again.

After Kiro fixes the source code, run the test again.

Ask Kiro to create a document.
```
Create a document on how to run the server and the test.
```

### Add New Features Using Kiro

Ask Kiro to add some features.
```
For all the pages, excluding the home page, insert a link back to the home page.
```

Run the test again to ensure that all the tests pass.

Ask Kiro to update the original features document.
```
Update the features file.
```

### Better Looking UI

Create a CSS Stylesheet.
```
Add a css stylesheet to make the ui looks better.
```

Change the placing of certain elements.
```
Place the link to the home page at the bottom right corner.
```

### Other Framework

Change the first line of the features.md to use other framework. For example:
```
# Sample Express Server with React Frontend
```

Alternatively, use the following prompt to Kiro.
```
Generate the source code according to the specification in ../express-server/docs/features.md but for flask. place the source code in the folder src/.
```

***
*Updated on 24 November 2025*
