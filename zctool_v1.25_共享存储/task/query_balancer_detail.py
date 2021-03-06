#!/usr/bin/python
from transaction.base_task import *
from service.message_define import *
from test_result_enum import *

class QueryBalancerDetailTask(BaseTask):
    operate_timeout = 5
    def __init__(self, task_type, messsage_handler,
                 case_manager,logger_name):
        self.case_manager = case_manager
        BaseTask.__init__(self, task_type, RequestDefine.query_balancer_detail,
                          messsage_handler, logger_name)
        
        self.addTransferRule(state_initial, AppMessage.RESPONSE,
                             RequestDefine.query_balancer_detail, result_success,
                             self.onRunSuccess)
        self.addTransferRule(state_initial, AppMessage.RESPONSE,
                             RequestDefine.query_balancer_detail, result_fail,
                             self.onRunFail)
        self.addTransferRule(state_initial, AppMessage.EVENT,
                             EventDefine.timeout, result_any,
                             self.onRunTimeout)        

    def invokeSession(self, session):
        """
        task start, must override
        """        
        request = getRequest(RequestDefine.query_balancer_detail)
        param = self.case_manager.getParam()
        control_server = param["control_server"]
        
        uuid  = param["uuid"]
        request.setString(ParamKeyDefine.uuid, uuid)       
        
        self.info("[%08X]request query balancer detail,uuid is '%s'"%
                       (session.session_id, uuid))
        
        request.session = session.session_id
        self.setTimer(session, self.operate_timeout)
        self.sendMessage(request, control_server)
        
    def onRunSuccess(self, msg, session):
        self.clearTimer(session)
        self.info("[%08X]query balancer detail success"%
                       (session.session_id))
        #print result
        ip = msg.getStringArray(ParamKeyDefine.ip)
        host = msg.getStringArray(ParamKeyDefine.host)
        name = msg.getStringArray(ParamKeyDefine.name)
        status = msg.getUIntArray(ParamKeyDefine.status)
        server = msg.getStringArray(ParamKeyDefine.server)

        nstatus = ChangeResuleStatus(status,Sturus_balancer_detail)

        title = ['IP','Host','Name','Status','Server']
        print_test_result(title,ip,host,name,nstatus,server)
        
        self.case_manager.finishTestCase(TestResultEnum.success)        
        session.finish()

    def onRunFail(self, msg, session):
        self.clearTimer(session)
        self.info("[%08X]query balancer detail fail"%
                  (session.session_id))
        self.case_manager.finishTestCase(TestResultEnum.fail)
        session.finish()
        
    def onRunTimeout(self, msg, session):
        self.info("[%08X]query balancer detail timeout"%
                  (session.session_id))
        self.case_manager.finishTestCase(TestResultEnum.timeout)
        session.finish()
