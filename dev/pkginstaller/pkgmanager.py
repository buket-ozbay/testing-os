def package_runner(cmd_arr):
    if cmd_arr[0] == "hello":
        try:
            import app.hello.hello
            app.hello.hello.run()
        except:
            print("This app is deleted")
    elif cmd_arr[0] == 'tester':
        try:
            import app.tester.main
            app.tester.main.run()
        except:
            print('This app is deleted')
