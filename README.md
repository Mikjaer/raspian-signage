Write the raspian to the sd-card:

# dd bs=4M if=2019-04-08-raspbian-stretch.img of=/dev/sde conv=fsync

When the command is done, run the sync command twice

# sync
# sync

Insert the flash-card and boot the raspberry bi, log in with username: pi and password: raspberry

Setup the rasperry as you normally would. (Timezone, Network, Root password and so on).


