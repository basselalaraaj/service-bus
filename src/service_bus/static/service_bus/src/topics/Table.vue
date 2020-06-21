<template>
  <ApolloQuery :query="GET_TOPIC_LIST">
    <template slot-scope="{ result: { loading, error, data } }">
      <!-- Loading -->
      <div v-if="loading">loading..</div>

      <!-- Error -->
      <div v-else-if="error">We got an error!</div>

      <!-- Result -->
      <div v-else-if="data">
        <v-data-table
          :headers="headers"
          :items="data.getTopicList"
          :loading="loading"
          loading-text="Loading... Please wait"
        >
          <template v-slot:item.name="{ item }">
            <router-link :to="{ path: 'topics/' + item.name }">{{ item.name }}</router-link>
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
      headers: [{ text: "Name", value: "name" }]
    }
  }
}
</script>
