
# Setting up Flask
In the termainl, we must type in and press ENTER:

`pip3 install flask`

# How to a set up a route that uses a HTML template

1. Create a folder named `templates` that is in the same level as your `app.y`

2. In the `templates` folder create a new file named `about.template.html` (or whatever you want your 
template file to be called)

3. Fill in the template as you deem fit.

4. Inside the view function, 

```
@app.route('/about')
def about_us():
    return render_template('about.template.html')
```