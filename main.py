import maya.cmds as cmds

def createJoint():
    j_number = cmds.intField(jointNumber, q=True, v=True)
    parentJ = ''
    curveSelected = cmds.ls(sl=True)[0]
    rootJnt =''

    for i in range(j_number):
        cmds.select(cl=True)
        newJ = cmds.joint()
        mp = cmds.pathAnimation(newJ, c=curveSelected, fm=True)
        cmds.cutKey(mp + '.u', time=())
        cmds.setAttr(mp + '.u', i * (1.0 / (j_number - 1)))
        cmds.delete(newJ+'.tx', icn=True)
        cmds.delete(newJ+'.ty', icn=True)
        cmds.delete(newJ+'.tz', icn=True)
        cmds.delete(mp)

        if i == 0:
            parentJ = newJ
            cmds.joint(newJ,e=True, oj = 'xyz', sao=)
            continue

        cmds.parent(newJ, parentJ)
        parentJ = newJ


if cmds.window('joint_Curve', exists=True):
    cmds.deleteUI('joint_Curve')

cmds.window('joint_Curve', title='Joint Along Curve', w=150)
cmds.columnLayout(adjustableColumn=True)
cmds.frameLayout(label='Select a curve', cll=False, bgc=[0.3, 0, 0.3], w=200)
jointNumber = cmds.intField(v=5, min=2)
cmds.checkBox('flexEst', label='Flexible estimate')
cmds.frameLayout(label='Orientation', cll=False, bgc=[0.3, 0, 0.3], w=200)
cmds.radioCollection()
cmds.button('create', c='createJoint()')
cmds.showWindow()
