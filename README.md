Edited for HILT 2018
--
# portfolio-stub
Stub site for use with our intro to GitHub

Steps:

1. Sign up for a GitHub account at https://github.com/join. You want your username to be descriptive of your digital identity. This will become your domain, so be mindful of that. For example, my GitHub username is walshbr.

n.b. - if you already have a GitHub account you can check in with us.

2. Verify your email address by clicking the link in the email you received.

3. Go to [this link](https://github.com/humanitiesprogramming/portfolio-stub): https://github.com/humanitiesprogramming/portfolio-stub

4. Click the fork button in the top right to copy the stub portfolio to your GitHub account. You'll be redirected to a new page after you're done.

5. Click the gear icon to access the "settings" for your new repository. In there, search for "repository name" and change it from "portfolio-stub" to be <username>.github.io, where <username> is your unique username. I.e., if your username is reedeth on GitHub your repository name would be reedeth.github.io. Click rename.

6. Click back to the "code" tab.

7. Look for the button that says "clone or download." Click it. Copy the link in it to your clipboard by either highlighting and copying or clicking the keyboard.

8. Switch to command line, and move to the place where you want to put the folder for your new repository. I.e., if I want it to be a folder on my Desktop, I would switch to ~/Desktop. Then clone it to your computer to copy it to your machine with git clone + the long slug you just copied to your clipboard. For example, in my case:

```
$ git clone https://github.com/walshtesting/walshtesting.github.io.git
```

9. This has made a copy of the files to your computer! Now change into the new repository (it will have the same name as the repository you copied):

```
$ cd walshtesting.github.io
```
10. Make a change to index.html - I'd suggest adding your name to the Title field.

```
$ git add .
$ git commit -m "The change I made"
$ git push
```

11. Visit <username>.github.io in your browser. Again, <username> should be replaced with your own username. I.e. walshbr.github.io for walshbr. You've got a portfolio live and on the internet! We won't customize this at all, but feel free to use this as a sandbox if you're interested in exploring HTML and CSS on your own. During the week we will just have you replicate a few tags to make a portfolio of the work you have done during the course.

12. Any future changes can be made with your standard workflow:

```
 **make a change**
$ git add .
$ git commit -m "The change I made"
$ git push
```
