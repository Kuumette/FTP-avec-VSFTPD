# CRÉER UN SERVEUR FTP AVEC VSFTPD

Dans cette partie nous allons voir les étapes pour créer un serveur FTP avec VSFTPD. Pour cela, vous pouvez découvrir une vidéo résumant l’installation :

[Video](https://www.youtube.com/watch?v=ZoAjFV5F86I&ab_channel=NumelionTutoriels)

Commençons à créer un serveur FTP avec VSFTPD. Dans un premier temps, nous allons créer un utilisateur FTP.

Vous remarquerez que la démonstration se réalise sur une machine Ubuntu avec un bureau gnome, donc il suffit de s’adapter si vous n’avez pas la même version. Vous devez vous rendre dans le menu : système -> administration -> utilisateurs et groupes.

Dans la nouvelle fenêtre qui s’ouvre, vous allez pouvoir créer votre utilisateur. Vous devez lui donner un nom puis un mot de passe. Mon utilisateur se nomme **ftp**.

## INSTALLATION DU SERVEUR

Vous allez devoir ouvrir un terminal. Vous devez passer en mode **superutilisateur** donc en root. Pour cela, vous devez utiliser la commande ` $ sudo su` puis votre mot de passe.

Ensuite, vous allez devoir installer le paquet vsftpd avec la commande `$ apt-get install vsftpd`. L’installation se lance, vous devez simplement patienter jusqu’à la fin.

Une fois l’installation terminée, vous allez devoir créer le répertoire **ftp**. Ce dernier sera utilisé par la suite. Vous pouvez utiliser la commande `$ mkdir /opt/ftp`. Il se créera donc dans le dossier **/opt**.

Maintenant, nous pouvons modifier le dossier de base de l’utilisateur FTP _(l’utilisateur crée précédemment)_ en le liant au nouveau répertoire que nous venons de créer.

Pour cela, vous devez utiliser la commande `$ usermod -d /opt/ftp ftp`.

Il nous reste à redémarrer le serveur FTP avec la commande `$ usermod -d /opt/ftp ftp`.

Nous allons créer un dossier test nommé artup. Le nom utilisé ici correspond à un projet, mais vous pouvez utiliser le nom que vous souhaitez. Il faut le créer dans le nouveau répertoire de l’utilisateur FTP. La commande est `$ mkdir /opt/ftp/artup`.

Vous pouvez vérifier que celui-ci est bien présent avec la commande `$ cd /opt/ftp` puis `$ ls »`.

Il nous reste à configurer VSFTP. On peut utiliser la commande `$ gedit /etc/vsftp.con` qui va nous permettre d’éditer le fichier de configuration.

Vérifiez ou modifiez les paramètres suivants :

-   `local_enable=YES`

-   `write_enable=YES`

-   `chroot_local_user=YES`

Une fois que vous avez terminé, vous devez enregistrer le fichier de configuration et redémarrer de nouveau le serveur `$ usermod -d /opt/ftp ftp`.

## SE CONNECTER SUR SON SERVEUR FTP

Désormais, le serveur est en place, vous allez pouvoir vous connecter depuis une autre machine. Pour cela, vous allez avoir besoin de l’adresse IP du serveur. On utilise la commande `$ ifconfig`. _Celui-ci a pour IP 192.168.1.103_.

![Drag Racing](https://www.numelion.com/images/stories/serveur-ftp-vsftpd/creer-un-serveur-ftp-14.JPG)
