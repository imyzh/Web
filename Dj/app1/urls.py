from django.urls import path
from app1 import views

urlpatterns = [

    path('', views.index.as_view()),
    path('userlogin', views.Login.as_view()),
    path('userall', views.UserAll.as_view()),
    path('userinfo', views.UserInfo.as_view()),
    path('historyevent', views.Historyeventinfo.as_view()),
    path('realtimeevent', views.Realtimeeventinfo.as_view()),
    # path('all', views.All.as_view()),
    # path('user/<int:id>', views.UserInfo.as_view())
    # re_path(r'^user/(.+)/$', views.UserInfo.as_view())
    
    # path('api/jwt/order', views.jwtOrder.as_view()),
    # path('api/jwt/order', views.jwtOrder.as_view()),
    # path('api/jwt/register', views.Register.as_view()),
    # path('v1/debug',debug1.as_view()),


    # path('order', views.Order.as_view()),
    # path('register', views.Register.as_view()),
    # path('alteruser', views.Alteruser.as_view()),
    
    # 文件管理
    # path('', TB_File.as_view()),
    # ## 视频设备管理接口
    # path('sensor/video/devregist', views.VideoDevice.as_view()),                                # 视频设备注册
    # path('sensor/video/devinfos',views.VideoDevice.as_view()),                                  # 视频设备查询
    # path('sensor/video/devdelete',views.VideoDel.as_view()),                                    # 视频设备信息删除
    # path('sensor/video/rec/query',views.QueryVideoHistory.as_view()),                           # 视频设备历史视频查询
    # ## 实时视频预览接口
    # path('sensor/video/live/view',views.ViewVideoLive.as_view()),                               # 实时视频预览
    # ## 视频分析任务接口
    # path('sensor/video/liveanalytask/submit',views.LiveVideoAnalysis.as_view()),                # 实时视频语义分析任务提交
    # path('sensor/video/liveanalytask/statequery',views.LiveVideoAnalysisState.as_view()),       # 实时视频语义分析任务状态查询
    # path('sensor/video/liveanalytask/query',views.LiveVideoAnalysisInfo.as_view()),             # 实时视频语义分析任务信息查询
    # path('sensor/video/liveanalytask/delete',views.LiveVideoAnalysisDelete.as_view()),          # 实时视频语义分析任务停止
    # path('sensor/video/analytask/eventlive',views.VideoAnalysisEvent.as_view()),                # 视频语义分析任务事件实时轮询
    # path('sensor/video/searchtask/img',views.ImgAnalysisSubmitEx.as_view()),                    # 实时视图像索任务提交
    # path('sensor/video/searchtask/query',views.ImgAnalysisQuery.as_view()),                     # 实时视频图像检索任务信息查询
    # path('sensor/video/searchtask/state',views.ImgAnalysisState.as_view()),                     # 实时视频图像检索任务状态查询
    # path('sensor/video/searchtask/liveresult',views.ImgAnalysisLiveResult.as_view()),           # 实时视频图像检索结果轮询
    # path('sensor/video/searchtask/cancel',views.ImgAnalysisCancel.as_view()),                   # 实时图像检索任务取消
]
