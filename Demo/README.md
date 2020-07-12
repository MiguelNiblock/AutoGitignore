In order to run, just call `python demo.py`. It'll look into the demo folders 1.0, 2.0, 3.0, it'll log the results and save them into a file named `result.gitignore`. 

### Custom Filename Result

You can generate a custom name if you specify it at `autoGI.save('CUSTOM_FILENAME')` within `demo.py`. For example, you might want it to already provide you with a hidden `.gitignore`. 

> It's currently set to `result.gitignore` to prevent it from potentially overwriting any existing `.gitignore` files, and for demo purposes.

### Custom Marker Search

To provide a different marker for files/folders to keep, specify it in `demo.py`  at `autoGI.run('CUSTOM_MARKER')`. For example, you might want to include all files and folders which contain a file named 'include.txt' or 'dockerfile', or anything.

