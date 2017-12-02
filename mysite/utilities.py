exclude_users_list = ['root', 'projmngr', 'netadmin', 'render', 'test', 'pip', 'prod', 'rtest', 'apache',
                      'zipcomp', 'it.admin', 'swnlayout', 'hr', 'it', 'nobody', 'swntex', 'auditor',
                      'video.conference', 'sysadmin', 'houdini.user', 'itsupport', 'layout', 'anim.user', 'aicstudio',
                      '', 'data.user', 'duser', 'lighting', 'nirav.patel', 'redhat.linux', 'swnanim', 'version.ase']


def get_user_info_from_ldap(arg_get_all_users_bln=False):
    import ldap
    
    ldap_server = "ldap://192.168.1.2"
    base_dn = "ou=People,dc=intra,dc=madassemblage,dc=com"
    
    ldap.set_option(ldap.OPT_REFERRALS, 0)
    Scope = ldap.SCOPE_SUBTREE
    Filter = "(uid=*)"
    # Attrs = ["cn", "uid"]
    Attrs = None
    
    name = ''
    l = ldap.initialize(ldap_server)
    
    r = l.search(base_dn, Scope, Filter, Attrs)
    Type, user_tuple = l.result(r, 60)
    # print 'Total Users: %s' % len(user_tuple)

    if arg_get_all_users_bln:
        return user_tuple

    user_info_list = list()
    for idx, user in enumerate(user_tuple):
        # print str(idx+1) + 50 * '-'
        uid = user[0]
        uinfo_dict = user[1]
        username_str = uinfo_dict['uid'][0]
        # print uinfo_dict
        displayname_str = uinfo_dict['cn'][0]
        store_info_dict = dict()
        # Result:
        # {'displayName': ['Project Manager'], 'cn': ['projmngr'], 'objectClass': ['top', 'person', 'organizationalPerson', 'posixAccount', 'shadowAccount', 'inetOrgPerson', 'sambaSamAccount'], 'loginShell': ['/bin/bash'], 'sambaHomeDrive': ['H:'], 'uidNumber': ['10003'], 'sambaSID': ['S-1-5-21-2617164855-2368010783-3780636620-515'], 'sambaAcctFlags': ['[XU         ]'], 'sambaPrimaryGroupSID': ['S-1-5-21-2617164855-2368010783-3780636620-512'], 'sambaDomainName': ['MADASSEMBLAGE'], 'gidNumber': ['10001'], 'gecos': ['System User'], 'sn': ['Manager'], 'homeDirectory': ['/home/projmngr'], 'sambaPwdLastSet': ['1387267257'], 'givenName': ['Project'], 'sambaNTPassword': ['E17290DE35D57912D70B533A6D977730'], 'uid': ['projmngr']}
        if username_str not in exclude_users_list:
            # print 'Addeding User: %s' % username_str
            store_info_dict['uid'] = username_str
            store_info_dict['cn'] = displayname_str
            user_info_list.append(store_info_dict)
    user_info_list = sorted(user_info_list, key=lambda k: k['uid'])
    l.unbind_s()
    return user_info_list

if __name__ == '__main__':
    ldap_user_info_list = get_user_info_from_ldap()
    print 'Total Usable Users: %s' % len(ldap_user_info_list)
    print 'Users: %s' % ldap_user_info_list
