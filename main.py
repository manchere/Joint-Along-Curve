import maya.cmds as cmds

def createJoint():
    jNumber = cmds.intField(jointNumber, q=True, v=True)
    for i in range(jNumber):
        mp = cmds.pathAnimation(cmds.joint(p=(0, 0, 0)), c=cmds.ls(sl=True)[0])
        cmds.cutKey(mp + '.u', time=())
        cmds.setAttr(mp + '.u', i * (1.0 /jNumber - 1))

if cmds.window('joint_Curve', exists=True):
    cmds.deleteUI('joint_Curve')

cmds.window('joint_Curve', title='Joint Along Curve', w=150)
cmds.columnLayout(adjustableColumn=True)
cmds.frameLayout(label='Select a curve', cll=False, bgc=[0.3, 0, 0.3], w=200)
jointNumber = cmds.intField(v=5)
cmds.button('create', c='createJoint')
cmds.showWindow()
