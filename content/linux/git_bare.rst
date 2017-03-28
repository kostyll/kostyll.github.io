Hot to setup remote git server ?
================================

1. Get/Generate custom ssh keys.
2. Add information about cutom host ssh keys to ~/.ssh/config file:

	.. code-block::bash
	host xxx.xxx.xxx.xxx
	 HostName xxx.xxx.xxx.xxx
	 IdentityFile ~/.ssh/XXX
	 User user

3. At server side create repo:

	.. code-block::bash
	cd /
	mkdir -p /opt/git/repo.git
	cd /opt/git/repo.git
	git init --bare

4. At client side make repo:

	.. code-block::bash
	cd /
	mkdir -p ~/repo
	cd ~/repo
	echo "testdata" > testfile.txt
	git add testfile.txt
	git commmit -m "initial commit"
	git remote add origing ssh://user@xxx.xxx.xxx.xxx:host_port/opt/git/repo.git
	git push origing master
