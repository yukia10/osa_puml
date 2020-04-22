
```puml
skinparam defaultTextAlignment center

!$OSA = "./osa"

!include $OSA/arrow_left.puml
!include $OSA/arrow_right.puml
!include $OSA/awareness.puml
!include $OSA/camera_web.puml
!include $OSA/cloud.puml
!include $OSA/contract.puml
!include $OSA/database.puml
!include $OSA/desktop.puml
!include $OSA/device_music.puml
!include $OSA/device_scanner.puml
!include $OSA/device_usb.puml
!include $OSA/device_usb_wifi.puml
!include $OSA/device_wireless_router.puml
!include $OSA/disposal.puml
!include $OSA/drive_harddisk.puml
!include $OSA/drive_optical.puml
!include $OSA/firewall.puml
!include $OSA/home.puml
!include $OSA/hub.puml
!include $OSA/iMac.puml
!include $OSA/iPhone.puml
!include $OSA/ics_drive.puml
!include $OSA/ics_plc.puml
!include $OSA/ics_thermometer.puml
!include $OSA/id_card.puml
!include $OSA/image.puml
!include $OSA/laptop.puml
!include $OSA/lifecycle.puml
!include $OSA/lightning.puml
!include $OSA/media_flash.puml
!include $OSA/media_optical.puml
!include $OSA/media_tape.puml
!include $OSA/mobile_pda.puml
!include $OSA/padlock.puml
!include $OSA/printer.puml
!include $OSA/server.puml
!include $OSA/server_application.puml
!include $OSA/server_database.puml
!include $OSA/server_directory.puml
!include $OSA/server_distribution.puml
!include $OSA/server_file.puml
!include $OSA/server_gateway.puml
!include $OSA/server_identity.puml
!include $OSA/server_mail.puml
!include $OSA/server_media.puml
!include $OSA/server_monitor.puml
!include $OSA/server_proxy.puml
!include $OSA/server_terminal.puml
!include $OSA/server_web.puml
!include $OSA/site_branch.puml
!include $OSA/site_factory.puml
!include $OSA/site_head_office.puml
!include $OSA/site_neighbourhood.puml
!include $OSA/user_architect.puml
!include $OSA/user_audit.puml
!include $OSA/user_black_hat.puml
!include $OSA/user_blue.puml
!include $OSA/user_business_manager.puml
!include $OSA/user_developer.puml
!include $OSA/user_green.puml
!include $OSA/user_operations.puml
!include $OSA/user_project_manager.puml
!include $OSA/user_security_specialist.puml
!include $OSA/user_service_manager.puml
!include $OSA/user_sysadmin.puml
!include $OSA/user_tester.puml
!include $OSA/user_tie.puml
!include $OSA/user_warning.puml
!include $OSA/user_white_hat.puml
!include $OSA/users_group.puml
!include $OSA/users_large_group.puml
!include $OSA/vpn.puml
!include $OSA/warning.puml
!include $OSA/wireless_network.puml
agent "arrow_left\n<$arrow_left{scale=0.5}>" as arrow_left
agent "arrow_right\n<$arrow_right{scale=0.5}>" as arrow_right
agent "awareness\n<$awareness{scale=0.5}>" as awareness
agent "camera_web\n<$camera_web{scale=0.5}>" as camera_web
agent "cloud\n<$cloud{scale=0.5}>" as cloud
agent "contract\n<$contract{scale=0.5}>" as contract
agent "database\n<$database{scale=0.5}>" as database
agent "desktop\n<$desktop{scale=0.5}>" as desktop
agent "device_music\n<$device_music{scale=0.5}>" as device_music
agent "device_scanner\n<$device_scanner{scale=0.5}>" as device_scanner
agent "device_usb\n<$device_usb{scale=0.5}>" as device_usb
agent "device_usb_wifi\n<$device_usb_wifi{scale=0.5}>" as device_usb_wifi
agent "device_wireless_router\n<$device_wireless_router{scale=0.5}>" as device_wireless_router
agent "disposal\n<$disposal{scale=0.5}>" as disposal
agent "drive_harddisk\n<$drive_harddisk{scale=0.5}>" as drive_harddisk
agent "drive_optical\n<$drive_optical{scale=0.5}>" as drive_optical
agent "firewall\n<$firewall{scale=0.5}>" as firewall
agent "home\n<$home{scale=0.5}>" as home
agent "hub\n<$hub{scale=0.5}>" as hub
agent "iMac\n<$iMac{scale=0.5}>" as iMac
agent "iPhone\n<$iPhone{scale=0.5}>" as iPhone
agent "ics_drive\n<$ics_drive{scale=0.5}>" as ics_drive
agent "ics_plc\n<$ics_plc{scale=0.5}>" as ics_plc
agent "ics_thermometer\n<$ics_thermometer{scale=0.5}>" as ics_thermometer
agent "id_card\n<$id_card{scale=0.5}>" as id_card
agent "image\n<$image{scale=0.5}>" as image
agent "laptop\n<$laptop{scale=0.5}>" as laptop
agent "lifecycle\n<$lifecycle{scale=0.5}>" as lifecycle
agent "lightning\n<$lightning{scale=0.5}>" as lightning
agent "media_flash\n<$media_flash{scale=0.5}>" as media_flash
agent "media_optical\n<$media_optical{scale=0.5}>" as media_optical
agent "media_tape\n<$media_tape{scale=0.5}>" as media_tape
agent "mobile_pda\n<$mobile_pda{scale=0.5}>" as mobile_pda
agent "padlock\n<$padlock{scale=0.5}>" as padlock
agent "printer\n<$printer{scale=0.5}>" as printer
agent "server\n<$server{scale=0.5}>" as server
agent "server_application\n<$server_application{scale=0.5}>" as server_application
agent "server_database\n<$server_database{scale=0.5}>" as server_database
agent "server_directory\n<$server_directory{scale=0.5}>" as server_directory
agent "server_distribution\n<$server_distribution{scale=0.5}>" as server_distribution
agent "server_file\n<$server_file{scale=0.5}>" as server_file
agent "server_gateway\n<$server_gateway{scale=0.5}>" as server_gateway
agent "server_identity\n<$server_identity{scale=0.5}>" as server_identity
agent "server_mail\n<$server_mail{scale=0.5}>" as server_mail
agent "server_media\n<$server_media{scale=0.5}>" as server_media
agent "server_monitor\n<$server_monitor{scale=0.5}>" as server_monitor
agent "server_proxy\n<$server_proxy{scale=0.5}>" as server_proxy
agent "server_terminal\n<$server_terminal{scale=0.5}>" as server_terminal
agent "server_web\n<$server_web{scale=0.5}>" as server_web
agent "site_branch\n<$site_branch{scale=0.5}>" as site_branch
agent "site_factory\n<$site_factory{scale=0.5}>" as site_factory
agent "site_head_office\n<$site_head_office{scale=0.5}>" as site_head_office
agent "site_neighbourhood\n<$site_neighbourhood{scale=0.5}>" as site_neighbourhood
agent "user_architect\n<$user_architect{scale=0.5}>" as user_architect
agent "user_audit\n<$user_audit{scale=0.5}>" as user_audit
agent "user_black_hat\n<$user_black_hat{scale=0.5}>" as user_black_hat
agent "user_blue\n<$user_blue{scale=0.5}>" as user_blue
agent "user_business_manager\n<$user_business_manager{scale=0.5}>" as user_business_manager
agent "user_developer\n<$user_developer{scale=0.5}>" as user_developer
agent "user_green\n<$user_green{scale=0.5}>" as user_green
agent "user_operations\n<$user_operations{scale=0.5}>" as user_operations
agent "user_project_manager\n<$user_project_manager{scale=0.5}>" as user_project_manager
agent "user_security_specialist\n<$user_security_specialist{scale=0.5}>" as user_security_specialist
agent "user_service_manager\n<$user_service_manager{scale=0.5}>" as user_service_manager
agent "user_sysadmin\n<$user_sysadmin{scale=0.5}>" as user_sysadmin
agent "user_tester\n<$user_tester{scale=0.5}>" as user_tester
agent "user_tie\n<$user_tie{scale=0.5}>" as user_tie
agent "user_warning\n<$user_warning{scale=0.5}>" as user_warning
agent "user_white_hat\n<$user_white_hat{scale=0.5}>" as user_white_hat
agent "users_group\n<$users_group{scale=0.5}>" as users_group
agent "users_large_group\n<$users_large_group{scale=0.5}>" as users_large_group
agent "vpn\n<$vpn{scale=0.5}>" as vpn
agent "warning\n<$warning{scale=0.5}>" as warning
agent "wireless_network\n<$wireless_network{scale=0.5}>" as wireless_network
arrow_left -[hidden]d-> device_scanner
device_scanner -[hidden]d-> hub
hub -[hidden]d-> lifecycle
lifecycle -[hidden]d-> server_application
server_application -[hidden]d-> server_monitor
server_monitor -[hidden]d-> user_audit
user_audit -[hidden]d-> user_service_manager
user_service_manager -[hidden]d-> warning
arrow_right -[hidden]d-> device_usb
device_usb -[hidden]d-> iMac
iMac -[hidden]d-> lightning
lightning -[hidden]d-> server_database
server_database -[hidden]d-> server_proxy
server_proxy -[hidden]d-> user_black_hat
user_black_hat -[hidden]d-> user_sysadmin
user_sysadmin -[hidden]d-> wireless_network
awareness -[hidden]d-> device_usb_wifi
device_usb_wifi -[hidden]d-> iPhone
iPhone -[hidden]d-> media_flash
media_flash -[hidden]d-> server_directory
server_directory -[hidden]d-> server_terminal
server_terminal -[hidden]d-> user_blue
user_blue -[hidden]d-> user_tester
camera_web -[hidden]d-> device_wireless_router
device_wireless_router -[hidden]d-> ics_drive
ics_drive -[hidden]d-> media_optical
media_optical -[hidden]d-> server_distribution
server_distribution -[hidden]d-> server_web
server_web -[hidden]d-> user_business_manager
user_business_manager -[hidden]d-> user_tie
cloud -[hidden]d-> disposal
disposal -[hidden]d-> ics_plc
ics_plc -[hidden]d-> media_tape
media_tape -[hidden]d-> server_file
server_file -[hidden]d-> site_branch
site_branch -[hidden]d-> user_developer
user_developer -[hidden]d-> user_warning
contract -[hidden]d-> drive_harddisk
drive_harddisk -[hidden]d-> ics_thermometer
ics_thermometer -[hidden]d-> mobile_pda
mobile_pda -[hidden]d-> server_gateway
server_gateway -[hidden]d-> site_factory
site_factory -[hidden]d-> user_green
user_green -[hidden]d-> user_white_hat
database -[hidden]d-> drive_optical
drive_optical -[hidden]d-> id_card
id_card -[hidden]d-> padlock
padlock -[hidden]d-> server_identity
server_identity -[hidden]d-> site_head_office
site_head_office -[hidden]d-> user_operations
user_operations -[hidden]d-> users_group
desktop -[hidden]d-> firewall
firewall -[hidden]d-> image
image -[hidden]d-> printer
printer -[hidden]d-> server_mail
server_mail -[hidden]d-> site_neighbourhood
site_neighbourhood -[hidden]d-> user_project_manager
user_project_manager -[hidden]d-> users_large_group
device_music -[hidden]d-> home
home -[hidden]d-> laptop
laptop -[hidden]d-> server
server -[hidden]d-> server_media
server_media -[hidden]d-> user_architect
user_architect -[hidden]d-> user_security_specialist
user_security_specialist -[hidden]d-> vpn
```
