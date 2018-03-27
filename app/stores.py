__metaclass__ = type


class BaseStore:
    def __init__(self,data_provider, last_id):
        self._data_provider = data_provider
        self._last_id = last_id

    def get_all(self):
        return self._data_provider

    def add(self,item_instance):
        item_instance.id = self.last_id
        self._data_provider.append(item_instance)
        self.last_id += 1

    def get_by_id(self, iden):
        all_members = self.get_all()
        for member in all_members:
            if iden is member.id:
                return member

    def entity_exists(self, item_instance):
        result = True
        if self.get_by_id(item_instance.id) is None:
            result = False

        return result

    def delete(self, iden):
        all_members = self.get_all()
        for member in all_members:
            if iden is member.id:
                all_members.remove(member)

    def update(self, item_instance):
        all_members = self.get_all()
        for member in all_members:
            if item_instance.id is member.id:
                self.delete(member.id)
                self._data_provider.append(item_instance)
                self._data_provider.sort(key=lambda members: member.id)


class MemberStore(BaseStore):

    members = []
    last_id = 1

    def __init__(self):
        super(MemberStore, self).__init__(MemberStore.members, MemberStore.last_id)

    def get_by_name(self, member_name):
        all_members = self.get_all()
        result = []
        for member in all_members:
            if member_name is member.name:
                 result.append(str(member))
        return result

    def get_members_with_posts(self, all_posts):
        all_members = self.get_all()

        for post in all_posts:
            for member in all_members:
                if post.member_id == member.id:
                    if post not in member.posts:
                        member.posts.append(post)
        return all_members

    def get_top_two(self, all_posts):
        all_members_posts = self.get_members_with_posts(all_posts)
        all_members_posts.sort(key=lambda member: len(member.posts), reverse=True)
        return all_members_posts


class PostStore(BaseStore):
    posts = []
    last_id = 1

    def __init__(self):
        super(PostStore, self).__init__(PostStore.posts, PostStore.last_id)

    def get_post_by_date(self):
        all_posts = self.get_all()
        all_posts.sort(key=lambda post: post.date, reverse=True)
        return all_posts
