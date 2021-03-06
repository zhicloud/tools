#!/usr/bin/python
#****************************************************************
#                               iso image
#****************************************************************

#modify_iso_image
"""
********modify_iso_image param*****
 -name(*): new iso image name.
 -id(*)  : iso image id of modify.
 -des    : describe of iso image.default:''
************************************
"""
param_modify_iso_image = {
    '-name' : None,
    '-id' : None,
    '-des' : ''
    }

#delete_iso_image
"""
********delete_iso_image param*****
 -id(*)   : iso image id of delete.
************************************
"""
param_delete_iso_image = {
    '-id' : None
    }

#upload_iso_image
"""
********upload_iso_image param*****
 -name: disk image name.
 -des    : describe of disk image.defalt:''
 -path      : shared memory path 
 -dt     : disk type
 -id     : 
************************************
"""
param_upload_iso_image = {
    '-name' : '',
    '-des' : '',
    '-path'   : '',
    '-dt'  : None,
    '-id'  : ''
    }
#****************************************************************
#                               media
#****************************************************************
#insert_media
"""
********insert_media param*****
 -id(*)  : host id.
 -image  : image uuid
************************************
"""
param_insert_media = {
    '-id' : None,
    '-image' : ''
    }

#change_media
"""
********change_media param*****
 -id(*)  : host id.
 -image  : image uuid
************************************
"""
param_change_media = {
    '-id' : None,
    '-image' : ''
    }

#eject_media
"""
********eject_media param*****
 -id(*)  : host id.
************************************
"""
param_eject_media = {
    '-id' : None,
    }
#****************************************************************
#                               disk image
#****************************************************************

#create_disk_image
"""
********create_disk_image param*****
 -name(*): disk image name.
 -id(*)  : host id of create disk.
 -des    : describe of disk image,default:''.
 -tag    : tag of disk image.
************************************
"""
param_create_disk_image = {
    '-name' : None,
    '-id' : None,
    '-des' : '',
    '-tag' : ''
    }

#modify_disk_image
"""
********modify_disk_image param*****
 -name(*): disk image name.
 -id(*)  : disk image id.
 -des     : describe of disk image,default:''.
************************************
"""
param_modify_disk_image = {
    '-name' : None,
    '-id' : None,
    '-des' : '',
    '-tag' : ''
    }

#delete_disk_image
"""
********delete_disk_image param*****
 -id(*) : disk image id.
************************************
"""
param_delete_disk_image = {
    '-id' : None
    }

#****************************************************************
#                               host
#****************************************************************
#create_host
"""
********create_host param*********
 -name(*): host name.
 -p(*)   : pool id.
 -c(*)   : cpu core.
 -m(*)   : memory.
 -d(*)   : system disk size(GB).
 -w      : monitor password,default:'123456'.
 -ui     : use disk image,0:false,1:true,default:'0'
 -mid    : image id,default:''.
 -ud     : use data disk,0:false,1:true,default:'0'.
 -au     : auto start 0:false 1:true,default:'0'.
 -bk     : backup host 0:false 1:true,default:'0'.
 -usb    : use usb 0:false 1:true,default:'0'.
 -ds     : data disk size(GB),default:'0'.
 -ib     : inbound width(MB),default:'2'.
 -ob     : outbound width(MB),default:'2'.
 -io     : host iops 0:false 1:true
 -pry    : cpu priority 0:high 1:Medium 2:low
 -count  : host count.
 -path   : ip san
 -crypt  : disk connection check information
 -h      : h264 0:false,1:true
**********************************
"""
param_create_host = {
    '-name' : None,
    '-p' : None,
    '-c' : None,
    '-m' : None,
    '-d' : None,
    '-w' : '123456',
    '-ui' : '0',
    '-mid' : '',
    '-ud' : '0',
    '-au' : '0',
    '-bk' : '',
    '-usb': '0',
    '-ds' : '0',
    '-ib' : '2',
    '-ob' : '2',
    '-port':'',
    '-net': '',
    '-io' : '0',
    '-pry': '0',
    '-count': '1',
    '-path' : '',
    '-crypt' : ''
    }

#start_host
"""
********start_host param*********
 -id(*) : host id.
 -iso   : iso image id.
 -b     : boot,0:local,1:CDROM,default:'0'.
*********************************
"""
param_start_host = {
    '-id' : None,
    '-iso' : '',
    '-b' : '0'
    }

#halt_host
"""
********halt_host param**********
 -id(*) : host id.
*********************************
"""
param_halt_host = {
    '-id' : None
    }
#reset_host
"""
********reset_host param*********
 -id(*) : host id.
*********************************
"""
param_reset_host = {
    '-id' : None
    }

#delete_host
"""
********delete_host param**********
 -id(*) : host id.
***********************************
"""
param_delete_host = {
    '-id' : None  
    }

#query_host
"""
********query_host param*********
 -p   : pool id.
 -d      : system disk size(GB).
 -mid    : image id,default:''.
 -au     : auto start,0:false,1:true,default:'0'.
 -p      : port,all:tcp&udp,or tcp/udp,default:'tcp:80,tcp:22'.
 -ib     : inbound width(MB),default:'2'.
 -ob     : outbound width(MB),default:'2'.
 -net    : connected virtual network, default:'reserved'
 -rg     : 0:compute pool 1:server
 -tg     : server id/pool id
**********************************
"""
param_query_host = {
    '-p' : '',
    '-mid' : '',
    '-d' : '10',  
    '-au' : '0',   
    '-port' : 'tcp:80,tcp:22',
    '-ib' : '2', 
    '-ob' : '2', 
    '-rg' : '0',
    '-tg' : ''
    }

#query_host_info
"""
********query_host_info param*********
 -id(*)   : host id.
**********************************
"""
param_query_host_info = {
    '-id' : None
    }

#stop_host
"""
********stop_host param**********
 -id(*) : host id.
*********************************
"""
param_stop_host = {
    '-id' : None
    }

#restart_host
"""
********restart_host param**********
 -id(*) : host id.
 -b(*):startup mode:0=hard disk;1=cd
 -mid(*):uuid of image
*********************************
"""
param_restart_host = {
    '-id' : None,
    '-b':'0',
    '-mid':''
    
    }

#modify_host
"""
********modify_host param********
 -id(*) :  host id.
 -name : host name
 -c  :  cpu core.
 -m  :  memory.
 -ds :  data disk size(GB).
 -w  :  monitor passwd,default:'123456'
 -au :  auto start 0:false 1:true,default:'0'.
 -bk : backup host 0:false 1:true,default:'0'.
 -usb: use usb 0:false 1:true,default:'0'.
 -p  :  port,default:''.
 -ib :  inbound width(Mb),default:''.
 -ob :  outbound width(Mb),default:''.
 -io     : host iops 0:false 1:true
 -pry    : cpu priority 0:high 1:Medium 2:low
*********************************
"""
param_modify_host = {
    '-id' : None,
    '-name' : '',
    '-c'  : '0',   
    '-m'  : '0',  
    '-ds' : '0',  
    '-w'  : '', 
    '-au' : '0',
    '-bk' : '0',
    '-usb': '0',  
    '-p'  : '', 
    '-ib' : '0',  
    '-ob' : '0',
    '-net': '',
    '-io' : '0',
    '-pry': '0'
    }
#migrate_host
"""
********migrate_host param********
    -id(*) : host uuid
    -t     : nc name (target)
    -type  : migrate type 0:cold 1:warm 2:hot
***********************************
"""
param_migrate_host = {
    '-id': None,
    '-t' : '',
    '-type' :'0'
    }

#****************************************************************
#                               service
#****************************************************************
#query_service
"""
*******query_service param*********
 -t(*) : type of query:
     2 : control service.
     3 : node client.
     4 : storage service.
 -g    : group of sercice,default:default.
***********************************
"""
param_query_service = {
    '-t' :None,
    '-g' :'default'
    }

#query_service_group
"""
*******query_service_group param*********
 -t(*) : type of query:
     2 : control service.
     3 : node client.
     4 : storage service.
***********************************
"""
param_query_service_group = {
    '-t' :None
    }
#modify_service
"""
*******modify_service param*********
 -t(*) : type of query:
     2 : control service.
     3 : node client.
     4 : storage service.
 -name : service name
 -dt : Shared memory disk type
 -ds : Shared memory disk source
 -c : Shared memory information 
***********************************
"""
param_modify_service = {
    '-t' :None,
    '-name' : '',
    '-dt' : '',
    '-ds' : '',
    '-c' : ''
    }
#enable_service
"""
*******enable_service param*********
 -t(*) : service name
***********************************
"""
param_enable_service= {
    '-t' :None
    }
#disable_service
"""
*******disable_service param*********
 -t(*) : service name
***********************************
"""
param_disable_service= {
    '-t' :None
    }

#****************************************************************
#                       compute_pool
#****************************************************************

#create_compute_pool
"""
create a computer pool
****create_compute_pool param*****
    -name(*) : compute resourece name.
    '-nt' : network type,
    '-nw' : network,
    '-dt' : disk type,
    '-ds' : disk_source
    '-qos': 1:true,0 false
    '-ha' : high_available 1:true,0 false
    '-thin': thin 1:true,0:false
    '-path':Shared memory path
    '-crypt':Shared memory information
***********************************
"""
param_create_compute_pool = {
    '-name' : None,
    '-nt' : None,
    '-nw' : '',
    '-dt' : '0',
    '-ds' : '',
    '-qos': '0',
    '-ha' : '0',
    '-thin': '0',
    '-path': '',
    '-crypt': ''

    }

#delete_compute_pool
"""
delete a computer pool.
****delete_compute_pool param*****
    -id(*) : compute pool uuid.
***********************************
eg:delete_compute_pool -id 060b8aff6fb04ca092534c6540425776
"""
param_delete_compute_pool = {
    '-id' : None
    }

#modify_compute_pool
"""
modify a computer pool informationl.
****modify_compute_pool param*****
    '-id' : computer pool uuid
    -name(*) : compute resourece name.
    '-nt' : network type
    '-nw' : network,
    '-dt' : disk type,
    '-ds' : disk_source
    '-op' : modify compute pool 1:true 0:false
    '-qos': 1:true,0 false
    '-thin': thin 1:true,0:false
    '-ha':high_available 1:true,0 false
    '-path':Shared memory path
    '-crypt':Shared memory information
***********************************
eg:modify_compute_pool -id 060b8aff6fb04ca092534c6540425776 -name abcdefg
"""
param_modify_compute_pool = {
    '-id' : None,
    '-name' : None,
    '-nt' : '0',
    '-nw' : '',
    '-dt' : '0',
    '-ds' : '',
    '-op' :'0',
    '-qos':'0',
    '-ha' :'0',
    '-thin':'0',
    '-path': '',
    '-crypt': ''
    }

#****************************************************************
#                       compute_resource
#****************************************************************

#add_compute_resource
"""
****add_compute_resource param*****
 -p(*)    : computer resource pool id.
 -name(*) : node client name.
***********************************
"""
param_add_compute_resource = {
    '-p' : None,
    '-name' : None
    }

#remove_compute_resource
"""
***remove_compute_resource param***
 -p(*)    : computer resource pool id.
 -name(*) : node client name.
***********************************
"""
param_remove_compute_resource = {
    '-p' : '',
    '-name' : ''
    }

#query_compute_resource
"""
***query_compute_resource param***
 -p(*)    : computer resource pool id.
***********************************
"""
param_query_compute_resource = {
    '-p' : '',
    }

"""
#**********************************************
#               port pool
#**********************************************
"""
#****************************************************************
#                       port pool
#****************************************************************
#create_port_pool
"""
create a port pool.
******create_port_pool param*******
 -name(*) : port pool name.
***********************************
eg:create_port_pool -name testportpool
"""
param_create_port_pool = {
    '-name' : None
    }

#delete_port_pool
"""
delete a port pool.
******delete_port_pool param*******
 -id(*) : port pool uuid.
***********************************
eg:delete_port_pool -id 31375fba19b64ea3b11effe6fc30e21a 
"""
param_delete_port_pool = {
    '-id' : None
    }

#add_port_resource
"""
add some ip address to port resource.
*****add_port_resource param*******
 -p(*)  : the port pool id want to add.
 -ip(*) : start ip address.
 -r(*)  : ip number
***********************************
eg:add_port_resource -p xxx -ip 202.105.182.213 -r 10
"""
param_add_port_resource = {
    '-p' : None,
    '-ip' : None,
    '-r' : None
    }

#remove_port_resource
"""
remove some ip address from port resource.
*****remove_port_resource param*******
 -p(*)  : the port pool id want to remove.
 -ip(*) : start ip address.
 -r(*)  : ip number
***********************************
eg:remove_port_resource -p 431ea0ce03df4256ac3b7d880af72ad6 -ip 202.105.182.213 -r 10
"""
param_remove_port_resource = {
    '-p' : None,
    '-ip' : None,
    '-r' : None
    }

#query_port_resource
"""
query port resource.
*****query_port_resource param*******
 -p(*)  : the port pool id.
***********************************
eg:query_port_resource -p 431ea0ce03df4256ac3b7d880af72ad6
"""
param_query_port_resource = {
    '-p' : None,
    }

"""
#**********************************************
#               forwarder
#**********************************************
"""
#****************************************************************
#                       forwarder
#****************************************************************

#add_forwarder
"""
********add_forwarder param********
    '-id' : target host uuid  
    '-t'  : target type,0=host, 1=disk   
    '-nt'  : network type,1:alone,2:share,  
    '-ns' : network source,address pool id 
*********************************
"""
param_add_forwarder = {
    '-id' : None,  
    '-t'  : '0',   
    '-nt'  : '2',  
    '-ns' : None 
    }

#remove_forwarder
"""
********remove_forwarder param********
    '-id' : target host uuid  
    '-t'  : target type,0=host, 1=disk   
    '-fid'  : forwarder id.  
*********************************
eg:remove_forwarder -id xx -t 0 -fid xx
"""
param_remove_forwarder = {
    '-id' : None,  
    '-t'  : '0',   
    '-fid'  : None 
    }


#query_forwarder
"""
query forwarder information.
*****query_forwarder param*******
  -type(*)  : forwarder type,0=mono,1=share,2=domain .
  -t        : group id/host id
***********************************
eg:query_forwarder -t 0
"""
param_query_forwarder = {
    '-type' : '0',
    '-t'    : ''
    }

#set_forwarder_status
"""
set forwarder status,0=disable,1=enable.
*****set_forwarder_status param*******
  -id(*)  : forwarder uuid .
  -s(*)   : forwarder status,0=disable,1=enable
***********************************
eg:set_forwarder_status -id xxxxx -s 0
"""
param_set_forwarder_status = {
    '-id' : None,
    '-s' : None
    }

#get_forwarder
"""
get forwarder information.
*****get_forwarder param*******
  -id(*)  : forwarder uuid .
***********************************
eg:get_forwarder -id xxxxx 
"""
param_get_forwarder = {
    '-id' : None,
    }






#query_forwarder_group
"""
get forwarder group information.
*****query_forwarder_group param*******
  -p(*)  : pool uuid .
***********************************
eg:query_forwarder -id xxxxx
"""
param_query_forwarder_group = {
    '-p' : None,
    }
#create_forwarder_group
"""
create forwarder group information.
*****create_forwarder_group param*******
  -p(*)  : pool uuid .
  -c     : forwarder num
***********************************
eg:create_forwarder_group -p xxxxx -c 1
"""
param_create_forwarder_group = {
    '-p' : None,
    '-c' : ''
    }
#delete_forwarder_group
"""
delete forwarder group information.
*****delete_forwarder_group param*******
  -id(*)  : pool uuid .
  -p      : option 0:false 1:true
***********************************
eg:delete_forwarder_group -id xxxxx -p 1
"""
param_delete_forwarder_group = {
    '-id' : None,
    '-p' : ''
    }

#create_forwarder
"""
create forwarder information.
*****create_forwarder param*******
  -id(*)  : forwarder group .
  -c     : forwarder num
***********************************
eg:create_forwarder -id xxxxx -c 1
"""
param_create_forwarder = {
    '-id' : None,
    '-c' : ''
    }

#delete_forwarder
"""
delete forwarder information.
*****delete_forwarder param*******
  -id(*)  : forwarder group .
  -t      : list of forwarder
***********************************
eg:delete_forwarder -id xxxxx -t 1
"""
param_delete_forwarder = {
    '-id' : None,
    '-t' : ''
    }

#attach_forwarder
"""
attach forwarder information.
*****attach_forwarder param*******
  -id(*)  : forwarder id .
  -type   : target type 
  -t      : host id
***********************************
eg:attach_forwarder -id xxxxx - type 0 -t xxx
"""
param_attach_forwarder = {
    '-id' : None,
    '-type' : '0',
    '-t'  : ''
    }

#detach_forwarder
"""
detach forwarder information.
*****detach_forwarder param*******
  -id(*)  : forwarder id .
  -type   : target type 
  -t      : host id
  -g      : forwarder group 
***********************************
eg:detach_forwarder -id xxxxx - type 0 -t xxx
"""
param_detach_forwarder = {
    '-id' : None,
    '-type' : '0',
    '-t'  : '',
    '-g'  : ''
    }
#migrate_forwarder
"""
migrate_forwarder information.
*****migrate_forwarder param*******
  -id(*)  : forwarder id .
  -t      : target:new address pool
  -ip     : list of new ip
***********************************
"""
param_migrate_forwarder = {
    '-id' : None,
    '-t'  : '',
    '-ip'  : ''
    }

#****************************************************************
#                       address_pool
#****************************************************************

#create_address_pool
"""
create an address pool.
******create_address_pool param*******
 -name(*) : address pool name.
***********************************
eg:create_address_pool -name mypool
"""
param_create_address_pool = {
    '-name' : None
    }
#delete_address_pool
"""
delete an address pool.
******delete_address_pool param*******
 -p(*) : address pool uuid.
***********************************
eg:delete_address_pool -p xxx
"""
param_delete_address_pool = {
    '-p' : None
    }
#add_address_resource
"""
add an address resource to pool.
******add_address_resource param*******
 -p(*): address pool uuid.
 -ip(*): starting ip.
 -r(*): count of ip.
***********************************
eg:add_address_resource -p xx -ip x.x.x.x -r 10
"""
param_add_address_resource = {
    '-p' : None,
    '-ip' : None,
    '-r' : None
    }
#remove_address_resource
"""
remove an address resource from pool.
******remove_address_resource param*******
 -p(*): address pool uuid.
 -ip(*): starting ip.
***********************************
eg:remove_address_resource -p xx -ip x.x.x.x
"""
param_remove_address_resource = {
    '-p' : '',
    '-ip' : ''
    }
#query_address_resource
"""
query address resource in pool.
******query_address_resource param*******
 -p(*): address pool uuid.
***********************************
eg:query_address_resource -p xxx
"""
param_query_address_resource = {
    '-p': None
    }

#****************************************************************
#                       storage_pool
#****************************************************************

#create_storage_pool
"""
creat a storage pool with specific use.
******create_storage_pool param*******
 -n(*): name of the storage_pool.
***********************************
eg:create_storage_pool -n storagepool-001 
"""
param_create_storage_pool = {
    '-n': None,
    }

#--------------------------------------------
#modify_storage_pool
"""
modify an existed storage pool.
******modify_storage_pool param*******
 -id(*) target storage pool uuid
 -n(*): name of the storage_pool.
***********************************
eg:modify_storage_pool -n storagepool-002 -id 
"""
param_modify_storage_pool = {
    '-id': None,
    '-n': None,
    }

#--------------------------------------------
#delete_storage_pool
"""
delete an existed storage pool.
******:delete_storage_pool param*******
 -id(*) target storage pool uuid
***********************************
eg::delete_storage_pool -id xxx
"""
param_delete_storage_pool = {
    '-id': None,
    }

#--------------------------------------------
#add_storage_resource
"""
add the resource storage pool to pool.
******:add_storage_resource param*******
 -p(*) storage pool uuid.
 -n(*) storage resource name.
***********************************
eg::add_storage_resource -p xx -n xx
"""
param_add_storage_resource = {
    '-p': None,
    '-n': None
    }

#--------------------------------------------
#remove_storage_resource
"""
remove the resource storage pool to pool.
******:remove_storage_resource param*******
 -p(*) storage pool uuid.
 -n(*) storage pool name.
***********************************
eg::remove_storage_resource -p xx -n xx
"""
param_remove_storage_resource = {
    '-p': None,
    '-n': None
    }

#--------------------------------------------
#query_storage_resource
"""
query the resource storage pool .
******:query_storage_resource param*******
 -p(*) storage pool uuid.
***********************************
eg::query_storage_resource -p xx 
"""
param_query_storage_resource = {
    '-p': None
    }
#--------------------------------------------
#start_monitor
"""
start monitor .
******:start_monitor param*******
 -n(*) storage resource name.
 -l    level.
***********************************
eg::start_monitor -n xx -l 5
"""
param_start_monitor = {
    '-n': '',
    '-l': '5'
    }

#stop_monitor
"""
stop monitor .
******:stop_monitor param*******
 -id(*) monitor task id.
***********************************
eg::stop_monitor -id xx
"""
param_stop_monitor = {
    '-id': None,
    }

#monitor_heart_beat
"""
monitor_heart_beat .
******:monitor_heart_beat param*******
 -id(*) monitor task id.
***********************************
eg::monitor_heart_beat -id xx
"""
param_monitor_heart_beat = {
    '-id': None,
    }
#monitor_data
"""
monitor_data .
******:monitor_data param*******
 -id(*) monitor task id.
***********************************
eg::monitor_data -id xx
"""
param_monitor_data = {
    '-id': None,
    #'-l': '5'
    }

#****************************************************************
#                       bind domain
#****************************************************************

#bind_domain
"""
bind domain.
******bind_domain param*******
 -n(*): name of the domain.
 -t: type,0=host,1=balancer,default 0
 -id(*): host/balancer id
***********************************
eg:bind_domain -n mydomain -t 0 -id xxx
"""
param_bind_domain = {
    '-n': None,
    '-t': '0',
    '-id': None
    }

#unbind_domain
"""
unbind domain.
******unbind_domain param*******
 -n(*): name of the domain.
***********************************
eg:unbind_domain -n mydomain
"""
param_unbind_domain = {
    '-n': None,
    }

#query_domain_name
"""
query domain name.
******query_domain_name param*******
 -ip(*): nallocated public ip.
***********************************
eg:query_domain_name -ip 10.11.11.11
"""
param_query_domain_name = {
    '-ip': None,
    }

#get_bound_domain
"""
get domain name.
******get_bound_domain param*******
 -n(*): url name.
***********************************
eg:get_bound_domain -n domain.zhicloue.com
"""
param_get_bound_domain = {
    '-n': None,
    }

#****************************************************************
#                       load_balancer
#****************************************************************

#disable_load_balancer
"""
disable aload_balancer.
******disable_load_balancer param*******
 -id(*): url name.
***********************************
eg:disable_load_balancer -id xxx
"""
param_disable_load_balancer = {
    '-id': None,
    }

#delete_load_balancer
"""
delete a load_balancer.
******delete_load_balancer param*******
 -id(*): url name.
***********************************
eg:delete_load_balancer -id xxx
"""
param_delete_load_balancer = {
    '-id': None,
    }

#attach_address
"""
attach a IP to load_balancer.
******attach_address param*******
    '-id': balancer id,
    '-p': address pool id,
    '-t': type,0=forwarder, 1=balancer
    '-c': count of need.
***********************************
eg:attach_address -id xxx -p xx -t 0 -c 5
"""
param_attach_address = {
    '-id': None,
    '-p': None,
    '-t': None,
    '-c': None
    }

#detach_address
"""
detach a IP from load_balancer.
******detach_address param*******
    '-t': type,0=forwarder, 1=balancer
    '-id': balancer id,
    '-ip': list of public ip,
***********************************
eg:detach_address -t 0 -ip 12.12.12.12 -id xxx
"""
param_detach_address = {
    '-t': None,
    '-ip': None,
    '-id': None
    }

#get_load_balancer
"""
get load balancer information.
******get_load_balancer param*******
    '-id': balancer id,
***********************************
eg:get_load_balancer -id xxx
"""
param_get_load_balancer = {
    '-id': None
    }

#query_load_balancer
"""
query load balancer information.
******query_load_balancer param*******
    '-t': query type,0=mono, 1=share,2=domain
***********************************
eg:query_load_balancer -t 0 
"""
param_query_load_balancer = {
    '-t': '0'
    }

#query_balancer_detail
"""
query load balancer information.
******query_balancer_detail param*******
    '-id': balancer id
***********************************
eg:query_balancer_detail -id xxx
"""
param_query_balancer_detail = {
    '-id': None
    }

#create_load_balancer
"""
create a load balancer.
******create_load_balancer param*******
 -n(*): name of the load balancer
 -t(*): type of the load balancer 0:mono,1:share
 -port: list of the  ordered host port.
***********************************
eg:create_load_balancer -n loadbalancer -t 0 -port 80
"""
param_create_load_balancer = {
    '-n': None,
    '-t': None,
    '-port': ''
    }
#add_balancer_node
"""
add a  balancer node.
******add_balancer_node param*******
 -id(*): uuid of the load balancer
 -h(*): uuid of the host 
 -n(*): name of the host
 -ip(*): ip of the server
 -port(*): list of the ordered server port
***********************************
eg:add_balancer_node -id xxx -h xxx -n xxx -ip 12.12.12.12 -port 122
"""
param_add_balancer_node = {
    '-id': None,
    '-h': None,
    '-n': None,
    '-ip': None,
    '-port': None
    }

#remove_balancer_node
"""
remove a  balancer node.
******remove_balancer_node param*******
 -id(*): uuid of the load balancer
 -h(*): uuid of the host 
***********************************
eg:remove_balancer_node -id xxx -h xxx
"""
param_remove_balancer_node = {
    '-id': None,
    '-h': None
    }

#modify_balancer_node
"""
modify a balancer node.
******modify_balancer_node param*******
 -id(*): uuid of the load balancer
 -h(*): uuid of the host 
 -ip(*): ip of the server
 -port(*): list of the ordered server port
***********************************
eg:modify_balancer_node -id xxx -h xxx -ip 12.12.12.12 -port 122
"""
param_modify_balancer_node = {
    '-id': None,
    '-h': None,
    '-ip': None,
    '-port': None
    }
#enable_load_balancer
"""
enable a load balancer.
******enable_load_balancer param*******
 -id(*): uuid of the load balancer
***********************************
eg:enable_load_balancer -id xxx
"""
param_enable_load_balancer = {
    '-id': None
    }

#query_server_rack
"""
********query_server_rack param*********
 -id(*)   : server room uuid.
**********************************
"""

param_query_server_rack = {
    '-id': None
    }

#query_server
"""
********query_server param*********
 -id(*)   : server rack uuid.
**********************************
"""

param_query_server = {
    '-id': None
    }
#attach_disk
"""
********attach_disk param*********
 -id(*)   : target host uuid.
 -dv(*)   :disk volume(Byte)
 -dt   :disk type(0=local 1=cloud,2=Nas,3=IP SAN)
 -ds   :disk resource,storage resouce uuid when disk type =cloud
 -m (*)   :disk mode(0=raw,1=ext3,2=ntfs)
 -path    :Shared memory path
 -crypt   :Shared memory info
**********************************
"""
param_attach_disk = {
    '-id': None,
    '-dv': None,
    '-dt': 0,
    '-ds': '',
    '-m': None,
    '-path': '',
    '-crypt': ''
    }
#detach_disk
"""
********detach_disk param*********
 -id(*)   : target host uuid.
 -index(*):disk index
  
**********************************
"""
param_detach_disk = {
    '-id': None,
    '-index': None
    }

#****************************************************************
#                       device
#****************************************************************
#query_device
"""
********query_device param*********
 -p(*)   : target storage pool uuid
 -t()   :query type(0=by pool) 
**********************************
"""
param_query_device = {
    '-p': None,
    '-t': '0'
    }
#create_device
"""
********create_device param*********
 -name(*)   : device name
 -p(*)   :storage pool uuid
 -dv(*): disk volume(MiB)
 -ps(*): page size(KiB)
 -rp(*): replication count
 -a():need authentication,0:false,1:true,default:0
 -et():encrypted transmit,0:false,1:true,default:0
 -ct():compressed transmit,0:false,1:true,default:0
 -es():encrypted storage,0:false,1:true,default:0
 -cs():compressed storage,0:false,1:true,default:0
 -pre():pre-allocate,0:false,1:true,default:0
 -dt(*): disk type 0=standard(100IOPS),1=speed(4000IOPS)
 -user():authentication account
 -pwd(): authentication password
 -crypt():encrypted key
 -ssid():snapshot pool uuid
**********************************
"""
param_create_device = {
    '-name': None,
    '-p': None,
    '-dv': None,
    '-ps': None,
    '-rp': None,
    '-a': '0',
    '-et': '0',
    '-ct': '0',
    '-es': '0',
    '-cs': '0',
    '-pre': '0',
    '-dt': None,
    '-user': '',
    '-pwd': '',
    '-crypt': '',
    '-ssid': ''
    
     }

#delete_device
"""
********delete_device param*********
 -id(*)   : target device uuid
**********************************
"""
param_delete_device = {
    '-id': None
    }

#modify_device
"""
********modify_device param*********
 -id(*)   : device uuid
 -name()   :device name
 -a():need authentication,0:false,1:true,default:0
 -et():encrypted transmit,0:false,1:true,default:0
 -ct():compressed transmit,0:false,1:true,default:0
 -dt(): disk type 0=standard(100IOPS),1=speed(4000IOPS)
 -user():authentication account
 -pwd(): authentication password
 -ssid():snapshot pool uuid
**********************************
"""
param_modify_device = {
    '-id': None,
    '-name': '',
    '-a': '0',
    '-et': '0',
    '-ct': '0',
    '-dt': '0',
    '-user': '',
    '-pwd': '',
    '-ssid': ''
    
     }
     
     
     
#****************************************************************
#                       snapshot
#****************************************************************     

#create_snapshot

"""
********create_snapshot param*********
 -name(*)   : snapshot name
 -tid(*)   :target device uuid
**********************************
"""
param_create_snapshot = {
    '-name': None,
    '-tid': None       
     }


#delete_snapshot

"""
********delete_snapshot param*********
 -id(*)   :snapshot uuid
**********************************
"""
param_delete_snapshot = {
    '-id': None       
     }

#resume_snapshot

"""
********resume_snapshot param*********
 -id(*)   :snapshot uuid
**********************************
"""
param_resume_snapshot = {
    '-id': None       
     }

#query_snapshot

"""
********query_snapshot param*********
 -tid(*)   :target device uuid
**********************************
"""
param_query_snapshot = {
    '-tid': None       
     }

#modify_snapshot_pool
"""
modify an existed snapshot pool.
******modify_snapshot_pool param*******
 -id(*) target snapshot pool uuid
 -n(*): name of the snapshot pool.
***********************************
eg:modify_snapshot_pool -n snapshotpool-002 -id 
"""
param_modify_snapshot_pool = {
    '-id': None,
    '-n': None,
    }

#create_snapshot_pool
"""
************** create_snapshot_pool ***********
     -n(*): name of the snapshot_pool.
	eg:create_snapshot_pool -n snapshotpool-001
***********************************************		 
"""
param_create_snapshot_pool = {
    '-n': None,
    }
#delete_snapshot_pool
"""
*************:delete_snapshot_pool param*******
         -id(*) target snapshot pool uuid
		 eg::delete_snapshot_pool -id xxx
***********************************************
"""
param_delete_snapshot_pool = {
    '-id': None,
    }
#query_snapshot_node
"""
query the node snapshot pool .
******:query_snapshot_node param*******
 -p(*) snapshot pool uuid.
***********************************
eg::query_snapshot_node -p xx 
"""
param_query_snapshot_node = {
    '-p': None
    }
#add_snapshot_node
"""
*************:add_snapshot_node param***********
         -p(*) snapshot pool uuid.
         -n(*) snapshot pool name.
		 eg::add_snapshot_pool -p xx -n xx
***********************************************
"""
param_add_snapshot_node = {
    '-p': None,
	'-n':None
    }
#remove_snapshot_node
"""	
*************remove_snapshot_node param********
         -p(*) snapshot pool uuid.
         -n(*) snapshot pool name.
		 eg::remove_snapshot_node -p xx -n xx
***********************************************
"""
param_remove_snapshot_node = {
    '-p': None,
	'-n':None
    }

#flush_disk_image
"""
flush_disk_image.
******:flush_disk_image param*******
 -id(*) host uuid.
 -dt(*) disk type(0=system disk 1=data disk)
 -mode() write from storage_server 
 -md(*) image uuid
 
***********************************
eg::flush_disk_image -id xx -dt 0 -mode 0 -md xx
"""

param_flush_disk_image = {
    '-id': None,
    '-md': None,
    '-dt': None,
    '-mode': '0',
    }
#backup_host
"""
backup_host.
******:backup_host param*******
 -id(*) host uuid.
 -md(*) back type(0=Full backup  1=Partial backup)
 -dt() disk type(0=system disk 1=data disk)
 
***********************************
eg::backup_host -id xx -md 0 -dt 0
"""
    
param_backup_host = {
    '-id': None,
    '-md': None,
    '-dt': '',  
    
    }
#resume_host
"""
resume_host.
******:resume_host param*******
 -id(*) host uuid.
 -md(*) back type(0=Full backup  1=Partial backup)
 -dt() disk type(0=system disk 1=data disk)
 
***********************************
eg::resume_host -id xx -md 0 -dt 0
"""
    
param_resume_host = {
    '-id': None,
    '-md': None,
    '-dt': '',    
    }
    
#query_host_backup
"""
query_host_backup.
******:query_host_backup param*******
 -id(*) host uuid.
 
***********************************
eg::query_host_backup -id xx 
"""
    
param_query_host_backup = {
    '-id': None
    }

#add_rule
"""
add_rule.
******:add_rule param*******
 -target(*) target IR name
 -mode(*) 0=INPUT rule  1=FORWARD rule 2=NAT rule
 -ip(*) 
 -port(*) 
 
***********************************
eg::add_rule -target xxx  -mode 0 -ip xxx -port xxx
"""
    
param_add_rule = {
    '-target': None,
    '-mode': None,
    '-ip': None,
    '-port': None
    }
#remove_rule
"""
remove_rule.
******:remove_rule param*******
 -target(*) target IR name
 -mode(*) 0=INPUT rule  1=FORWARD rule 2=NAT rule
 -ip(*) 
 -port(*) 
 
***********************************
eg::remove_rule -target xxx  -mode 0 -ip xxx -port xxx
"""
    
param_remove_rule = {
    '-target': None,
    '-mode': None,
    '-ip': None,
    '-port': None
    }
#query_rule
"""
query_rule.
******:query_rule param*******
 -t(*) target IR name
***********************************
eg::query_rule -t xxx
"""
    
param_query_rule = {
    '-t': None
    }

#VPC
#create_network
"""
create_network.
******:create_network param*******
 -p(*) address pool id
 -n(*) VPC name
 -ns(*) subnet mask;
 -des  description
***********************************
eg::create_network -p xxx -n xxx -ns xxx
"""
param_create_network = {
    '-p': None,
    '-n': None,
    '-ns': None,
    '-des':''
    }
#modify_network
"""
modify_network.
******:modify_network param*******
 -id(*) VPC uuid
 -n(*) VPC name
 -des  description
 -p compute pool uuid
 -ip ip list
 -op modify compute pool 1:true 0:false
***********************************
eg::modify_network -p xxx -n xxx -ns xxx
"""
param_modify_network = {
    '-id': None,
    '-n': None,
    '-des':'',
    '-p' : '',
    '-ip': '',
    '-op': '0',
    }
#query_network_detail
"""
query_network_detail
******:query_network_detail param*******
 -id(*) vpc uuid
***********************************
eg::query_network_detail -id xxx 
"""
param_query_network_detail = {
    '-id' : None
    }

#start_network
"""
start_network
******:start_network param*******
 -id(*) vpc uuid
***********************************
eg::start_network -id xxx 
"""
param_start_network = {
    '-id' : None
    }
#stop_network
"""
stop_network
******:stop_network param*******
 -id(*) vpc uuid
***********************************
eg::stop_network -id xxx 
"""
param_stop_network = {
    '-id' : None
    }
#delete_network
"""
delete_network
******:delete_network param*******
 -id(*) vpc uuid
***********************************
eg::delete_network -id xxx 
"""
param_delete_network = {
    '-id' : None
    }
#query_network_host
"""
query_network_host
******:query_network_host param*******
 -id(*) vpc uuid
***********************************
eg::query_network_host -id xxx 
"""
param_query_network_host = {
    '-id' : None
    }
#attach_host
"""
attach_host
******:attach_host param*******
 -id(*) vpc uuid
 -host(*) host uuid
***********************************
eg::attach_host -id xxx  -host xxx
"""
param_attach_host = {
    '-id' : None,
    '-host' : None
    }
#detach_host
"""
detach_host
******:detach_host param*******
 -id(*) vpc uuid
 -host(*) host uuid
***********************************
eg::detach_host -id xxx  -host xxx
"""
param_detach_host = {
    '-id' : None,
    '-host' : None
    }
#network_attach_address
"""
network_attach_address
******:network_attach_address param*******
 -id(*) vpc uuid
 -count(*) host uuid
***********************************
eg::network_attach_address -id xxx  -count xxx
"""
param_network_attach_address = {
    '-id' : None,
    '-count' : None
    }
#network_detach_address
"""
network_detach_address
******:network_detach_address param*******
 -id(*) vpc uuid
 -ip(*) detach ip
***********************************
eg::network_detach_address -id xxx  -count xxx
"""
param_network_detach_address = {
    '-id' : None,
    '-ip' : None
    }
#network_bind_port
"""
network_bind_port
******:network_bind_port param*******
 -id(*) vpc uuid
 -port(*) bind port
***********************************
eg::network_bind_port -id xxx  -port xxx
"""
param_network_bind_port = {
    '-id' : None,
    '-port' : None
    }
#network_unbind_port
"""
network_unbind_port
******:network_unbind_port param*******
 -id(*) vpc uuid
 -port(*) bind port
***********************************
eg::network_unbind_port -id xxx  -port xxx
"""
param_network_unbind_port = {
    '-id' : None,
    '-port' : None
    }
#query_operate_detail
"""
query_operate_detail
******:query_operate_detail param*******
 -t(*) target
 -l(*) query level
 -begin begin time 
 -end  end time 
***********************************
eg::query_operate_detail -t xxx  -l xxx
"""

param_query_operate_detail = {
    '-t' : None,
    '-l' : None,
    '-begin' : None,
    '-end' : None
    }

#query_operate_summary
"""
query_operate_summary
******:query_operate_summary param*******
 -t(*) target
 -begin begin time 
 -end  end time 
***********************************
eg::query_operate_summary -t xxx 
"""
param_query_operate_summary = {
    '-t' : None,
    '-begin' : None,
    '-end' : None
    }
#query_service_detail
"""
query_service_detail
******:query_service_detail param*******
 -t(*) target
 -l(*) query level
 -begin begin time 
 -end  end time 
***********************************
eg::query_service_detail -t xxx  -l xxx
"""

param_query_service_detail = {
    '-t' : None,
    '-l' : None,
    '-begin' : None,
    '-end' : None
    }
#query_service_summary
"""
query_service_summary
******:query_service_summary param*******
 -t(*) target
 -begin begin time 
 -end  end time 
***********************************
eg::query_service_summary -t xxx
"""

param_query_service_summary = {
    '-t' : None,
    '-begin' : None,
    '-end' : None
    }

"""
query_compute_pool_detail
******:query_compute_pool_detail param*******
     -id(*) compute_pool uuid
***********************************
eg::query_compute_pool_detail -p  xxx
    """
    
param_query_compute_pool_detail = {
    '-id' : None
    }

#****************************************************************
#                       storage_device
#****************************************************************     


#query_storage_device
"""
********query_stoage_device param*********
 -l      : Target level.
 -t      : Target type.
 -d (*)  : disk_type.
     0   : Local storage
     1   : Cloud storage
     2   : NAS
     3   : IP SAN
**********************************
eg::query_storage -l 0 -t XXX -d 0
"""
param_query_storage_device = {
    '-l' : '0',
    '-t' : None,
    '-d' : None
    }
#add_storage_device
"""
********add_storage_device param*********
 -l      : Target level.
 -t      : Target type.
 -d (*)  : disk_type.
     0   : Local storage
     1   : Cloud storage
     2   : NAS
     3   : IP SAN
 -i      : To mount the disk index list
 -n      : Path identifier name
 -p      : Shared memory path required to connect
 -c      : Shared memory connection information
**********************************
eg::add_storage_device -l 0 -t XXX -d 0 -i XXX
"""
param_add_storage_device = {
    '-l' : '0',
    '-t' : None,
    '-d' : None,
    '-i' : '',
    '-n' : '',
    '-p' : '',
    '-c' : ''
    }
#remove_storage_device
"""
********remove_storage_device param*********
 -l      : Target level.
 -t      : Target type.
 -d (*)  : disk_type.
     0   : Local storage
     1   : Cloud storage
     2   : NAS
     3   : IP SAN
 -i      : To mount the disk index list
**********************************
eg::remove_storage_device -l 0 -t XXX -d 0 -i XXX
"""
param_remove_storage_device = {
    '-l' : '0',
    '-t' : None,
    '-d' : None,
    '-i' : None
    }

#enable_storage_device
"""
********enable_storage_device param*********
 -l      : Target level.
 -t      : Target type.
 -d (*)  : disk_type.
     0   : Local storage
     1   : Cloud storage
     2   : NAS
     3   : IP SAN
 -i      : To mount the disk index list
**********************************
eg::enable_storage_device -l 0 -t XXX -d 0 -i XXX
"""
param_enable_storage_device = {
    '-l' : '0',
    '-t' : None,
    '-d' : None,
    '-i' : None
    }
#disable_storage_device
"""
********disable_storage_device param*********
 -l      : Target level.
 -t      : Target type.
 -d (*)  : disk_type.
     0   : Local storage
     1   : Cloud storage
     2   : NAS
     3   : IP SAN
 -i      : To mount the disk index list
**********************************
eg::disable_storage_device -l 0 -t XXX -d 0 -i XXX
"""
param_disable_storage_device = {
    '-l' : '0',
    '-t' : None,
    '-d' : None,
    '-i' : None
    }



    
