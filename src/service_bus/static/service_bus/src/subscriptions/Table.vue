<template>
  <ApolloQuery
    :query="GET_SUBSCRIPTION_LIST"
    :variables="{
      topic
    }"
  >
    <template slot-scope="{ result: { loading, error, data } }">
      <!-- Loading -->
      <div v-if="!data && !error">loading..</div>

      <!-- Error -->
      <div v-if="error">We got an error!</div>

      <!-- Result -->
      <div v-if="data">
        <v-data-table
          :headers="headers"
          :items="data.getSubscriptionList"
          :loading="loading"
          loading-text="Loading... Please wait"
        >
          <template v-slot:item.name="{ item }">
            <router-link
              :to="{
                name: 'dlq-messages-messages',
                params: { topic: topic, subscription: item.name }
              }"
              >{{ item.name }}</router-link
            >
          </template>
        </v-data-table>
      </div>
    </template>
  </ApolloQuery>
</template>

<script>
import gql from "graphql-tag"
const GET_SUBSCRIPTION_LIST = gql`
  query GetSubscriptionList($topic: String) {
    getSubscriptionList(topic: $topic) {
      name
    }
  }
`
export default {
  data() {
    return {
      GET_SUBSCRIPTION_LIST: GET_SUBSCRIPTION_LIST,
      headers: [{ text: "Name", value: "name" }],
      topic: this.$route.params.topic
    }
  }
}
</script>
