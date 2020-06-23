<template>
  <ApolloQuery
    :query="GET_DLQ_MESSAGES"
    :variables="{
      topic,
      subscription
    }"
  >
    <template slot-scope="{ result: { loading, error, data } }">
      <!-- Loading -->
      <div v-if="loading">loading..</div>

      <!-- Error -->
      <div v-else-if="error">We got an error!</div>

      <!-- Result -->
      <div v-else-if="data">
        <v-data-table
          :headers="headers"
          :items="data.getDlqMessages"
          :loading="loading"
          loading-text="Loading... Please wait"
        >
          <template v-slot:item.name="{ item }">
            {{ item.body }}
          </template>
        </v-data-table>
      </div>
    </template>
  </ApolloQuery>
</template>

<script>
import gql from "graphql-tag"
const GET_DLQ_MESSAGES = gql`
  query GetDlqMessages($topic: String, $subscription: String) {
    getDlqMessages(topic: $topic, subscription: $subscription) {
      body
    }
  }
`
export default {
  data() {
    return {
      GET_DLQ_MESSAGES: GET_DLQ_MESSAGES,
      headers: [{ text: "Name", value: "name" }],
      topic: this.$route.params.topic,
      subscription: this.$route.params.subscription
    }
  }
}
</script>
