# New Computer Install Script

# Features Needed

- Install i3wm
- Set up terminal colors
- Set up bashrc aliases
- Set up keyboard shortcuts
- Install latex / bibtex

    ```bash
    sudo apt install latexmk
    sudo apt install texlive-latex-extra
    sudo apt install texlive-bibtex-extra
    ```

- Install programs

    ```bash
    # Programs
    sudo apt install vim
    sudo apt install vscode
    sudo apt install feh
    sudo apt install compton
    sudo apt install i3blocks
    sudo apt install rofi

    # Python
    sudo apt install python3
    sudo apt install python3-pip
    pip3 install numpy
    pip3 install scipy
    pip3 install matplotlib
    pip3 install pandas
    pip3 install sklearn
    pip3 install jupyter

    # Fsearch
    sudo add-apt-repository ppa:christian-boxdoerfer/fsearch-daily
    sudo apt install fsearch-trunk
    ```

    - spotify
    - Rstudio
    - Anaconda - [https://www.anaconda.com/download/#linux](https://www.anaconda.com/download/#linux)
- Set up SSH keys and aliases

    ```bash
    ssh-keygen -t rsa
    ```

- Git pull all of the things I need / set up git

    ```bash
    git config --global user.email "samsledje@gmail.com"
    git config --global user.name "Samuel Sledzieski"
    git pull git@gitlab.com:samsledje/config-files.git
    cd config-files
    ln -s bashrc ~/.bashrc
    ln -s vimrc ~/.vimrc
    ln -s ssh_config ~/.ssh/config
    mkdir -p ~/.config/i3
    ln -s i3config ~/.config/i3/config
    ln -s i3blocks ~/.config/i3/i3blocks.conf
    cd ~
    ```

# Notes

[Initialize start-up applications in certain workspaces?](https://askubuntu.com/questions/431086/initialize-start-up-applications-in-certain-workspaces)