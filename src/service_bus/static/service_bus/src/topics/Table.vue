<template>
  <ApolloQuery :query="GET_TOPIC_LIST">
    <template slot-scope="{ result: { loading, error, data } }">
      <!-- Loading -->
      <div v-if="!data && !error">loading..</div>

      <!-- Error -->
      <div v-if="error">We got an error!</div>

      <!-- Result -->
      <div v-if="data">
        <v-data-table
          :headers="headers"
          :items="data.getTopicList"
          :loading="loading"
          loading-text="Loading... Please wait"
        >
          <template v-slot:item.name="{ item }">
            <router-link
              :to="{ name: 'dlq-messages-subscriptions', params: { topic: item.name } }"
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
const GET_TOPIC_LIST = gql`
  query GetTopicList {
    getTopicList {
      name
    }
  }
`
export default {
  data() {
    return {
      GET_TOPIC_LIST: GET_TOPIC_LIST,
      headers: [{ text: "Topic", value: "name" }]
    }
  }
}
</script>
